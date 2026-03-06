from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from models.models import FoodListing, DonorRating
from datetime import datetime
from utils.notify import send_notification, notify_recipients_of_donation
import os, math

foodbank = Blueprint('foodbank', __name__, url_prefix='/foodbank')

HYDERABAD_LOCATIONS = [
    {'name': 'Banjara Hills',    'lat': 17.4156, 'lng': 78.4347},
    {'name': 'Jubilee Hills',    'lat': 17.4326, 'lng': 78.4071},
    {'name': 'Hitech City',      'lat': 17.4435, 'lng': 78.3772},
    {'name': 'Gachibowli',       'lat': 17.4401, 'lng': 78.3489},
    {'name': 'Madhapur',         'lat': 17.4486, 'lng': 78.3908},
    {'name': 'Secunderabad',     'lat': 17.4399, 'lng': 78.4983},
    {'name': 'Begumpet',         'lat': 17.4448, 'lng': 78.4627},
    {'name': 'Kukatpally',       'lat': 17.4947, 'lng': 78.3996},
    {'name': 'KPHB Colony',      'lat': 17.4912, 'lng': 78.3943},
    {'name': 'Ameerpet',         'lat': 17.4374, 'lng': 78.4486},
    {'name': 'Dilsukhnagar',     'lat': 17.3688, 'lng': 78.5247},
    {'name': 'LB Nagar',         'lat': 17.3453, 'lng': 78.5520},
    {'name': 'Mehdipatnam',      'lat': 17.3956, 'lng': 78.4375},
    {'name': 'Tolichowki',       'lat': 17.4047, 'lng': 78.4086},
    {'name': 'Manikonda',        'lat': 17.4085, 'lng': 78.3898},
    {'name': 'Kondapur',         'lat': 17.4600, 'lng': 78.3615},
    {'name': 'Miyapur',          'lat': 17.4965, 'lng': 78.3548},
    {'name': 'Nizampet',         'lat': 17.5120, 'lng': 78.4031},
    {'name': 'Uppal',            'lat': 17.4059, 'lng': 78.5591},
    {'name': 'Nagole',           'lat': 17.3866, 'lng': 78.5612},
    {'name': 'Kompally',         'lat': 17.5498, 'lng': 78.4817},
    {'name': 'Alwal',            'lat': 17.4849, 'lng': 78.5009},
    {'name': 'Bowenpally',       'lat': 17.4707, 'lng': 78.4883},
    {'name': 'Musheerabad',      'lat': 17.4257, 'lng': 78.5037},
    {'name': 'Narayanguda',      'lat': 17.3982, 'lng': 78.4852},
    {'name': 'Himayatnagar',     'lat': 17.4030, 'lng': 78.4796},
    {'name': 'Abids',            'lat': 17.3850, 'lng': 78.4867},
    {'name': 'Nampally',         'lat': 17.3806, 'lng': 78.4735},
    {'name': 'Charminar',        'lat': 17.3616, 'lng': 78.4747},
    {'name': 'Old City',         'lat': 17.3546, 'lng': 78.4698},
]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

@foodbank.route('/')
@login_required
def index():
    for l in FoodListing.query.filter_by(status='available').all():
        if l.is_expired:
            l.status = 'expired'
    db.session.commit()

    category = request.args.get('category', '')
    sort     = request.args.get('sort', 'newest')

    q = FoodListing.query.filter_by(status='available')
    if category:
        q = q.filter_by(category=category)
    if sort == 'expiry':
        q = q.order_by(FoodListing.expiry_date.asc())
    else:
        q = q.order_by(FoodListing.posted_at.desc())

    listings = q.all()

    if sort == 'distance' and current_user.lat and current_user.lng:
        listings.sort(key=lambda l: haversine(current_user.lat, current_user.lng,
                                               l.latitude or 17.385, l.longitude or 78.486))

    map_data = [{'id': l.id, 'name': l.food_name, 'qty': l.quantity,
                 'loc': l.location, 'lat': l.latitude or 17.385,
                 'lng': l.longitude or 78.486,
                 'exp': l.hours_to_expiry} for l in listings]

    return render_template('foodbank/index.html',
                           listings=listings, map_data=map_data,
                           category=category, sort=sort)

@foodbank.route('/donate', methods=['GET', 'POST'])
@login_required
def donate():
    if request.method == 'POST':
        loc_name = request.form.get('location', '').strip()
        lat = float(request.form.get('latitude') or 17.3850)
        lng = float(request.form.get('longitude') or 78.4867)

        preset = next((l for l in HYDERABAD_LOCATIONS if l['name'] == loc_name), None)
        if preset:
            lat, lng = preset['lat'], preset['lng']

        photo_url = None
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo and photo.filename:
                fname = f"{current_user.id}_{int(datetime.utcnow().timestamp())}_{photo.filename}"
                save_path = os.path.join('static', 'uploads', fname)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                photo.save(save_path)
                photo_url = f"/static/uploads/{fname}"

        expiry_str = request.form.get('expiry_date', '')
        try:
            expiry = datetime.strptime(expiry_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            expiry = None

        listing = FoodListing(
            donor_id    = current_user.id,
            food_name   = request.form.get('food_name', '').strip(),
            category    = request.form.get('category', ''),
            quantity    = request.form.get('quantity', '').strip(),
            expiry_date = expiry,
            location    = loc_name,
            latitude    = lat,
            longitude   = lng,
            description = request.form.get('description', '').strip(),
            photo_url   = photo_url,
            allergens   = '',
            status      = 'available',
        )
        db.session.add(listing)
        db.session.flush()  # get listing.id before commit

        # ── Notify all recipients about the new donation ──────────────────
        notify_recipients_of_donation(listing)
        # ─────────────────────────────────────────────────────────────────

        db.session.commit()
        flash('Food listed successfully! 🎉 Thank you for donating!', 'success')
        return redirect(url_for('foodbank.index'))

    return render_template('foodbank/donate.html', locations=HYDERABAD_LOCATIONS)

@foodbank.route('/claim/<int:listing_id>')
@login_required
def claim(listing_id):
    listing = FoodListing.query.get_or_404(listing_id)
    if listing.status != 'available':
        flash('This item is no longer available.', 'danger')
        return redirect(url_for('foodbank.index'))
    listing.status     = 'claimed'
    listing.claimed_by = current_user.id
    listing.claimed_at = datetime.utcnow()

    # Notify the donor that their listing was claimed
    send_notification(
        user_id = listing.donor_id,
        type_   = 'claim',
        title   = f'🙌 {current_user.name} claimed your donation!',
        body    = f'Your listing "{listing.food_name}" has been claimed.',
        link    = url_for('foodbank.my_donations')
    )
    db.session.commit()
    flash(f'You claimed {listing.food_name}! Contact the donor to arrange pickup. 🙌', 'success')
    return redirect(url_for('foodbank.index'))

@foodbank.route('/pickup/<int:listing_id>')
@login_required
def mark_pickup(listing_id):
    listing = FoodListing.query.get_or_404(listing_id)
    if listing.claimed_by == current_user.id and listing.status == 'claimed':
        listing.status       = 'picked_up'
        listing.picked_up_at = datetime.utcnow()

        send_notification(
            user_id = listing.donor_id,
            type_   = 'pickup',
            title   = f'✅ Pickup confirmed for "{listing.food_name}"',
            body    = f'{current_user.name} has picked up your donation.',
            link    = url_for('foodbank.my_donations')
        )
        db.session.commit()
        flash('Pickup confirmed! Please rate the donor. 🌟', 'success')
        return redirect(url_for('foodbank.rate_donor', listing_id=listing_id))
    flash('Action not allowed.', 'danger')
    return redirect(url_for('foodbank.my_claims'))

@foodbank.route('/rate/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def rate_donor(listing_id):
    listing = FoodListing.query.get_or_404(listing_id)
    if request.method == 'POST':
        rating  = int(request.form.get('rating', 5))
        comment = request.form.get('comment', '').strip()
        dr = DonorRating(listing_id=listing_id, donor_id=listing.donor_id,
                         rater_id=current_user.id, rating=rating, comment=comment)
        db.session.add(dr)
        all_ratings = DonorRating.query.filter_by(donor_id=listing.donor_id).all()
        listing.donor_rating = sum(r.rating for r in all_ratings) / len(all_ratings)
        db.session.commit()
        flash('Thank you for rating! ⭐', 'success')
        return redirect(url_for('foodbank.my_claims'))
    return render_template('foodbank/rate.html', listing=listing)

@foodbank.route('/my-donations')
@login_required
def my_donations():
    listings = FoodListing.query.filter_by(donor_id=current_user.id)\
                                .order_by(FoodListing.posted_at.desc()).all()
    total_kg      = sum(2 for l in listings if l.status in ['claimed','picked_up'])
    total_claimed = sum(1 for l in listings if l.status in ['claimed','picked_up'])
    return render_template('foodbank/my_donations.html',
                           listings=listings,
                           total_kg=total_kg,
                           total_claimed=total_claimed)

@foodbank.route('/my-claims')
@login_required
def my_claims():
    listings = FoodListing.query.filter_by(claimed_by=current_user.id)\
                                .order_by(FoodListing.claimed_at.desc()).all()
    return render_template('foodbank/my_claims.html', listings=listings)

@foodbank.route('/delete/<int:listing_id>', methods=['POST'])
@login_required
def delete_listing(listing_id):
    listing = FoodListing.query.filter_by(id=listing_id, donor_id=current_user.id).first_or_404()
    db.session.delete(listing)
    db.session.commit()
    flash('Listing deleted.', 'info')
    return redirect(url_for('foodbank.my_donations'))