"""
translations.py — All UI strings for English, Telugu, and Hindi
Add new keys here, then use {{ t.key_name }} in any Jinja2 template.
"""

TRANSLATIONS = {

    # ── ENGLISH ──────────────────────────────────────────────────────────────
    'en': {
        # Nav
        'nav_dashboard':    'Dashboard',
        'nav_diet':         'Diet',
        'nav_exercise':     'Exercise',
        'nav_foodbank':     'Food Bank',
        'nav_progress':     'Progress',
        'nav_admin':        'Admin',
        'nav_login':        'Login',
        'nav_logout':       'Logout',
        'nav_get_started':  'Get Started',

        # Landing page
        'hero_line1':       'Eat Smart.',
        'hero_line2':       'Move Well.',
        'hero_line3':       'Give Back.',
        'hero_sub':         "India's first AI platform combining sustainable diet, fitness & community food donation.",
        'hero_cta':         '🚀 Get Started Free',
        'hero_donate':      '🤝 Donate Food',
        'stat_food_saved':  'KG Food Saved',
        'stat_meals':       'Meals Provided',
        'stat_users':       'Active Users',
        'stat_co2':         'KG CO₂ Saved',
        'modules_title':    'One Platform. Three Superpowers.',
        'modules_sub':      'Everything you need to live healthy and sustainably.',
        'mod_diet_title':   'Sustainable Diet Planner',
        'mod_diet_desc':    'AI generates a personalized 7-day meal plan with carbon footprint scores for every meal.',
        'mod_ex_title':     'Fitness & Exercise Planner',
        'mod_ex_desc':      'Get a weekly workout plan linked to your diet goal.',
        'mod_food_title':   'Community Food Bank',
        'mod_food_desc':    'Connect surplus food with people in need on a live map.',
        'explore':          'Explore →',
        'sdg_title':        '🎯 Supporting 6 UN Sustainable Development Goals',
        'cta_title':        'Ready to FeedForward?',
        'cta_sub':          'Join thousands building a healthier, more sustainable life.',
        'cta_btn':          '🌱 Start for Free',

        # Dashboard
        'dash_morning':     'Good Morning',
        'dash_afternoon':   'Good Afternoon',
        'dash_evening':     'Good Evening',
        'dash_subtitle':    "Here's your health snapshot for today",
        'dash_new_diet':    '🔄 New Diet Plan',
        'dash_new_ex':      '🔄 New Exercise Plan',
        'dash_streak':      'Workout Streak',
        'dash_weight':      'Current Weight (kg)',
        'dash_cal':         "Today's Calories",
        'dash_carbon':      'Carbon Score (kg CO₂)',
        'dash_meals_title': "Today's Meals",
        'dash_view_plan':   'View Full Plan →',
        'dash_workout':     "Today's Workout",
        'dash_rest_day':    '😴 Rest Day — Recovery is important!',
        'dash_food_title':  'Available Food Near You',
        'dash_view_map':    'View Map →',
        'dash_log_title':   "Log Today's Progress",
        'dash_no_plan':     'Complete your profile to get personalized plans.',

        # Diet
        'diet_title':       '🥗 Sustainable Diet Planner',
        'diet_sub':         'Your AI-generated 7-day carbon-conscious meal plan',
        'diet_regen':       '🔄 Regenerate Plan',
        'diet_target_cal':  'Target Calories/Day',
        'diet_avg_cal':     'Avg Daily Calories',
        'diet_avg_carbon':  'Avg Daily Carbon (kg CO₂)',
        'diet_bmr':         'Your BMR (kcal)',
        'diet_week_plan':   '📅 Your 7-Day Meal Plan',
        'diet_breakfast':   'Breakfast',
        'diet_lunch':       'Lunch',
        'diet_dinner':      'Dinner',
        'diet_snack':       'Snack',
        'diet_swap_title':  '♻️ Greener Swap Suggestions',
        'diet_swap_sub':    'These meals have the lowest carbon footprint:',
        'diet_no_plan':     'No Meal Plan Yet',
        'diet_no_plan_sub': 'Complete your profile to get your personalized sustainable meal plan.',

        # Exercise
        'ex_title':         '💪 Exercise Planner',
        'ex_sub':           'Your personalized weekly workout plan',
        'ex_regen':         '🔄 Regenerate Plan',
        'ex_bmi_title':     '📊 Your BMI',
        'ex_water_title':   '💧 Daily Water Target',
        'ex_week_plan':     '📅 Your Weekly Workout Plan',
        'ex_rest_day':      'Rest & Recovery Day',
        'ex_rest_msg':      "Rest is when your muscles grow. Stay hydrated!",
        'ex_watch':         '▶ Watch Video',
        'ex_no_plan':       'No Exercise Plan Yet',

        # Food Bank
        'fb_title':         '🤝 Community Food Bank',
        'fb_sub':           'Connect surplus food with people in need — live map',
        'fb_donate_btn':    '+ Donate Food',
        'fb_my_donations':  'My Donations',
        'fb_my_claims':     'My Claims',
        'fb_map_title':     '🗺️ Live Food Map',
        'fb_listings':      '🍱 Available Food Listings',
        'fb_claim':         '🙌 Claim Food',
        'fb_your_donation': 'Your Donation',
        'fb_no_listings':   'No Food Listings Yet',
        'fb_no_list_sub':   'Be the first to donate! Every bit of food saved matters.',
        'fb_donate_now':    'Donate Food Now',

        # Progress
        'prog_title':       '📊 Progress Tracker',
        'prog_streak':      'Workout Streak',
        'prog_logs':        'Total Logs',
        'prog_weight':      'Latest Weight',
        'prog_water':       'Last Water (L)',
        'prog_log_title':   "📝 Log Today's Progress",
        'prog_weight_lbl':  'Weight (kg)',
        'prog_water_lbl':   'Water Intake (litres)',
        'prog_cal_in':      'Calories Consumed',
        'prog_cal_out':     'Calories Burned',
        'prog_mood':        "Today's Mood",
        'prog_workout':     'Workout completed today ✅',
        'prog_notes':       'Notes (optional)',
        'prog_save':        '💾 Save Progress',
        'prog_chart_wt':    '⚖️ Weight Over Time',
        'prog_chart_cal':   '🔥 Calories In vs Out',
        'prog_history':     '📅 Log History',
        'prog_date':        'Date',
        'prog_no_logs':     'No logs yet. Start logging today!',

        # Profile setup
        'setup_title':      'Set Up Your Profile',
        'setup_sub':        "We'll generate your personalized plans instantly",
        'setup_personal':   '👤 Personal Info',
        'setup_diet':       '🥗 Diet Preferences',
        'setup_fitness':    '💪 Fitness Info',
        'setup_generate':   '🚀 Generate My Plans →',
        'setup_age':        'Age (years)',
        'setup_gender':     'Gender',
        'setup_weight':     'Weight (kg)',
        'setup_height':     'Height (cm)',
        'setup_location':   'Your City / Location',
        'setup_diet_pref':  'Dietary Preference',
        'setup_goal':       'Health Goal',
        'setup_level':      'Fitness Level',
        'setup_equipment':  'Equipment Available',
        'setup_days':       'Workout Days/Week',

        # Auth
        'login_title':      'Welcome Back',
        'login_sub':        'Login to your FeedForward account',
        'login_email':      'Email Address',
        'login_password':   'Password',
        'login_btn':        'Login →',
        'login_no_acct':    'No account?',
        'login_register':   'Register here',
        'reg_title':        'Join FeedForward',
        'reg_sub':          'Create your free account',
        'reg_name':         'Full Name',
        'reg_role':         'I want to join as',
        'reg_btn':          'Create Account →',
        'reg_have_acct':    'Already have an account?',

        # Footer
        'footer_tagline':   'Eat Smart. Move Well. Give Back.',
        'footer_built':     'Built with ❤️ for Innovathon 2025 | Python + Flask',

        # Common
        'save':             'Save',
        'cancel':           'Cancel',
        'delete':           'Delete',
        'edit':             'Edit Profile',
        'available':        'Available',
        'claimed':          'Claimed',
        'expired':          'Expired',
        'low_carbon':       'Low Carbon ✅',
        'mood_great':       '😄 Great',
        'mood_good':        '🙂 Good',
        'mood_okay':        '😐 Okay',
        'mood_bad':         '😔 Bad',
    },

    # ── TELUGU ───────────────────────────────────────────────────────────────
    'te': {
        # Nav
        'nav_dashboard':    'డాష్‌బోర్డ్',
        'nav_diet':         'ఆహారం',
        'nav_exercise':     'వ్యాయామం',
        'nav_foodbank':     'ఆహార బ్యాంక్',
        'nav_progress':     'పురోగతి',
        'nav_admin':        'అడ్మిన్',
        'nav_login':        'లాగిన్',
        'nav_logout':       'లాగ్అవుట్',
        'nav_get_started':  'ప్రారంభించండి',

        # Landing
        'hero_line1':       'తెలివిగా తినండి.',
        'hero_line2':       'ఆరోగ్యంగా ఉండండి.',
        'hero_line3':       'తిరిగి ఇవ్వండి.',
        'hero_sub':         'స్థిరమైన ఆహారం, ఫిట్‌నెస్ మరియు సమాజ ఆహార దానం కలిపే మొట్టమొదటి AI ప్లాట్‌ఫారమ్.',
        'hero_cta':         '🚀 ఉచితంగా ప్రారంభించండి',
        'hero_donate':      '🤝 ఆహారం దానం చేయండి',
        'stat_food_saved':  'KG ఆహారం ఆదా',
        'stat_meals':       'అందించిన భోజనాలు',
        'stat_users':       'క్రియాశీల వినియోగదారులు',
        'stat_co2':         'KG CO₂ ఆదా',
        'modules_title':    'ఒకే ప్లాట్‌ఫారమ్. మూడు శక్తులు.',
        'modules_sub':      'ఆరోగ్యంగా మరియు స్థిరంగా జీవించడానికి అవసరమైనవన్నీ.',
        'mod_diet_title':   'స్థిరమైన ఆహార ప్రణాళికకర్త',
        'mod_diet_desc':    'AI మీకు 7 రోజుల వ్యక్తిగతీకరించిన భోజన ప్రణాళికను కార్బన్ స్కోర్‌తో రూపొందిస్తుంది.',
        'mod_ex_title':     'ఫిట్‌నెస్ & వ్యాయామ ప్రణాళికకర్త',
        'mod_ex_desc':      'మీ ఆహార లక్ష్యానికి అనుగుణంగా వారపు వ్యాయామ ప్రణాళికను పొందండి.',
        'mod_food_title':   'సమాజ ఆహార బ్యాంక్',
        'mod_food_desc':    'అదనపు ఆహారాన్ని అవసరమైన వారితో లైవ్ మ్యాప్‌లో కనెక్ట్ చేయండి.',
        'explore':          'అన్వేషించండి →',
        'sdg_title':        '🎯 6 UN స్థిరమైన అభివృద్ధి లక్ష్యాలకు మద్దతు',
        'cta_title':        'FeedForward కు సిద్ధంగా ఉన్నారా?',
        'cta_sub':          'ఆరోగ్యకరమైన, స్థిరమైన జీవితం కోసం వేలాది మందితో చేరండి.',
        'cta_btn':          '🌱 ఉచితంగా ప్రారంభించండి',

        # Dashboard
        'dash_morning':     'శుభోదయం',
        'dash_afternoon':   'శుభ మధ్యాహ్నం',
        'dash_evening':     'శుభ సాయంత్రం',
        'dash_subtitle':    'ఈరోజు మీ ఆరోగ్య సారాంశం',
        'dash_new_diet':    '🔄 కొత్త ఆహార ప్రణాళిక',
        'dash_new_ex':      '🔄 కొత్త వ్యాయామ ప్రణాళిక',
        'dash_streak':      'వ్యాయామ స్ట్రీక్',
        'dash_weight':      'ప్రస్తుత బరువు (kg)',
        'dash_cal':         'ఈరోజు కేలరీలు',
        'dash_carbon':      'కార్బన్ స్కోర్ (kg CO₂)',
        'dash_meals_title': 'ఈరోజు భోజనాలు',
        'dash_view_plan':   'పూర్తి ప్రణాళిక చూడండి →',
        'dash_workout':     'ఈరోజు వ్యాయామం',
        'dash_rest_day':    '😴 విశ్రాంతి రోజు — రికవరీ ముఖ్యం!',
        'dash_food_title':  'మీ దగ్గర అందుబాటులో ఉన్న ఆహారం',
        'dash_view_map':    'మ్యాప్ చూడండి →',
        'dash_log_title':   'ఈరోజు పురోగతి నమోదు చేయండి',
        'dash_no_plan':     'వ్యక్తిగతీకరించిన ప్రణాళికలు పొందడానికి మీ ప్రొఫైల్‌ను పూర్తి చేయండి.',

        # Diet
        'diet_title':       '🥗 స్థిరమైన ఆహార ప్రణాళికకర్త',
        'diet_sub':         'మీ AI రూపొందించిన 7-రోజుల కార్బన్-స్పృహ భోజన ప్రణాళిక',
        'diet_regen':       '🔄 ప్రణాళికను పునరుత్పత్తి చేయండి',
        'diet_target_cal':  'లక్ష్య కేలరీలు/రోజు',
        'diet_avg_cal':     'సగటు రోజువారీ కేలరీలు',
        'diet_avg_carbon':  'సగటు కార్బన్ (kg CO₂)',
        'diet_bmr':         'మీ BMR (kcal)',
        'diet_week_plan':   '📅 మీ 7-రోజుల భోజన ప్రణాళిక',
        'diet_breakfast':   'అల్పాహారం',
        'diet_lunch':       'మధ్యాహ్న భోజనం',
        'diet_dinner':      'రాత్రి భోజనం',
        'diet_snack':       'స్నాక్',
        'diet_swap_title':  '♻️ పచ్చని మార్పిడి సూచనలు',
        'diet_swap_sub':    'ఈ భోజనాలకు అతి తక్కువ కార్బన్ పాదముద్ర ఉంది:',
        'diet_no_plan':     'భోజన ప్రణాళిక లేదు',
        'diet_no_plan_sub': 'మీ ప్రొఫైల్‌ను పూర్తి చేయండి.',

        # Exercise
        'ex_title':         '💪 వ్యాయామ ప్రణాళికకర్త',
        'ex_sub':           'మీ వ్యక్తిగతీకరించిన వారపు వ్యాయామ ప్రణాళిక',
        'ex_regen':         '🔄 ప్రణాళికను పునరుత్పత్తి చేయండి',
        'ex_bmi_title':     '📊 మీ BMI',
        'ex_water_title':   '💧 రోజువారీ నీరు లక్ష్యం',
        'ex_week_plan':     '📅 మీ వారపు వ్యాయామ ప్రణాళిక',
        'ex_rest_day':      'విశ్రాంతి & రికవరీ రోజు',
        'ex_rest_msg':      'విశ్రాంతి సమయంలో కండరాలు పెరుగుతాయి. నీరు తాగండి!',
        'ex_watch':         '▶ వీడియో చూడండి',
        'ex_no_plan':       'వ్యాయామ ప్రణాళిక లేదు',

        # Food Bank
        'fb_title':         '🤝 సమాజ ఆహార బ్యాంక్',
        'fb_sub':           'అదనపు ఆహారాన్ని అవసరమైన వారితో కనెక్ట్ చేయండి',
        'fb_donate_btn':    '+ ఆహారం దానం చేయండి',
        'fb_my_donations':  'నా దానాలు',
        'fb_my_claims':     'నా క్లెయిమ్‌లు',
        'fb_map_title':     '🗺️ లైవ్ ఆహార మ్యాప్',
        'fb_listings':      '🍱 అందుబాటులో ఉన్న ఆహారం',
        'fb_claim':         '🙌 ఆహారం తీసుకోండి',
        'fb_your_donation': 'మీ దానం',
        'fb_no_listings':   'ఆహార జాబితాలు లేవు',
        'fb_no_list_sub':   'మొదట దానం చేయండి! ఆదా చేసిన ప్రతి ఆహారం ముఖ్యమైనది.',
        'fb_donate_now':    'ఇప్పుడు ఆహారం దానం చేయండి',

        # Progress
        'prog_title':       '📊 పురోగతి ట్రాకర్',
        'prog_streak':      'వ్యాయామ స్ట్రీక్',
        'prog_logs':        'మొత్తం లాగ్‌లు',
        'prog_weight':      'తాజా బరువు',
        'prog_water':       'చివరి నీరు (L)',
        'prog_log_title':   '📝 ఈరోజు పురోగతి నమోదు చేయండి',
        'prog_weight_lbl':  'బరువు (kg)',
        'prog_water_lbl':   'నీరు తాగారు (లీటర్లు)',
        'prog_cal_in':      'తీసుకున్న కేలరీలు',
        'prog_cal_out':     'కాల్చిన కేలరీలు',
        'prog_mood':        'ఈరోజు మూడ్',
        'prog_workout':     'ఈరోజు వ్యాయామం చేశారు ✅',
        'prog_notes':       'గమనికలు (ఐచ్ఛికం)',
        'prog_save':        '💾 పురోగతి సేవ్ చేయండి',
        'prog_chart_wt':    '⚖️ బరువు మార్పు',
        'prog_chart_cal':   '🔥 కేలరీలు అందుకున్న vs కాల్చిన',
        'prog_history':     '📅 లాగ్ చరిత్ర',
        'prog_date':        'తేదీ',
        'prog_no_logs':     'ఇంకా లాగ్‌లు లేవు. ఈరోజు ప్రారంభించండి!',

        # Profile setup
        'setup_title':      'మీ ప్రొఫైల్ సెటప్ చేయండి',
        'setup_sub':        'మేము వెంటనే వ్యక్తిగతీకరించిన ప్రణాళికలను రూపొందిస్తాము',
        'setup_personal':   '👤 వ్యక్తిగత సమాచారం',
        'setup_diet':       '🥗 ఆహార ప్రాధాన్యతలు',
        'setup_fitness':    '💪 ఫిట్‌నెస్ సమాచారం',
        'setup_generate':   '🚀 నా ప్రణాళికలను రూపొందించండి →',
        'setup_age':        'వయస్సు (సంవత్సరాలు)',
        'setup_gender':     'లింగం',
        'setup_weight':     'బరువు (kg)',
        'setup_height':     'ఎత్తు (cm)',
        'setup_location':   'మీ నగరం / స్థానం',
        'setup_diet_pref':  'ఆహార ప్రాధాన్యత',
        'setup_goal':       'ఆరోగ్య లక్ష్యం',
        'setup_level':      'ఫిట్‌నెస్ స్థాయి',
        'setup_equipment':  'అందుబాటులో ఉన్న పరికరాలు',
        'setup_days':       'వ్యాయామ రోజులు/వారం',

        # Auth
        'login_title':      'తిరిగి స్వాగతం',
        'login_sub':        'మీ FeedForward ఖాతాలోకి లాగిన్ చేయండి',
        'login_email':      'ఇమెయిల్ చిరునామా',
        'login_password':   'పాస్‌వర్డ్',
        'login_btn':        'లాగిన్ →',
        'login_no_acct':    'ఖాతా లేదా?',
        'login_register':   'ఇక్కడ నమోదు చేయండి',
        'reg_title':        'FeedForward లో చేరండి',
        'reg_sub':          'మీ ఉచిత ఖాతాను సృష్టించండి',
        'reg_name':         'పూర్తి పేరు',
        'reg_role':         'నేను చేరాలనుకుంటున్నాను',
        'reg_btn':          'ఖాతా సృష్టించండి →',
        'reg_have_acct':    'ఇప్పటికే ఖాతా ఉందా?',

        # Footer
        'footer_tagline':   'తెలివిగా తినండి. ఆరోగ్యంగా ఉండండి. తిరిగి ఇవ్వండి.',
        'footer_built':     'Innovathon 2025 కోసం ❤️ తో నిర్మించబడింది | Python + Flask',

        # Common
        'save':             'సేవ్ చేయండి',
        'cancel':           'రద్దు చేయండి',
        'delete':           'తొలగించండి',
        'edit':             'ప్రొఫైల్ సవరించండి',
        'available':        'అందుబాటులో ఉంది',
        'claimed':          'తీసుకోబడింది',
        'expired':          'గడువు ముగిసింది',
        'low_carbon':       'తక్కువ కార్బన్ ✅',
        'mood_great':       '😄 చాలా బాగుంది',
        'mood_good':        '🙂 బాగుంది',
        'mood_okay':        '😐 సాధారణం',
        'mood_bad':         '😔 చెడ్డగా ఉంది',
    },

    # ── HINDI ─────────────────────────────────────────────────────────────────
    'hi': {
        # Nav
        'nav_dashboard':    'डैशबोर्ड',
        'nav_diet':         'आहार',
        'nav_exercise':     'व्यायाम',
        'nav_foodbank':     'फूड बैंक',
        'nav_progress':     'प्रगति',
        'nav_admin':        'एडमिन',
        'nav_login':        'लॉगिन',
        'nav_logout':       'लॉगआउट',
        'nav_get_started':  'शुरू करें',

        # Landing
        'hero_line1':       'समझदारी से खाएं।',
        'hero_line2':       'अच्छे से चलें।',
        'hero_line3':       'वापस दें।',
        'hero_sub':         'भारत का पहला AI प्लेटफॉर्म जो टिकाऊ आहार, फिटनेस और सामुदायिक खाद्य दान को एक साथ जोड़ता है।',
        'hero_cta':         '🚀 मुफ्त में शुरू करें',
        'hero_donate':      '🤝 खाना दान करें',
        'stat_food_saved':  'KG खाना बचाया',
        'stat_meals':       'भोजन प्रदान किए',
        'stat_users':       'सक्रिय उपयोगकर्ता',
        'stat_co2':         'KG CO₂ बचाया',
        'modules_title':    'एक प्लेटफॉर्म। तीन शक्तियां।',
        'modules_sub':      'स्वस्थ और टिकाऊ जीवन जीने के लिए सब कुछ।',
        'mod_diet_title':   'टिकाऊ आहार योजनाकार',
        'mod_diet_desc':    'AI आपके लिए 7-दिन की व्यक्तिगत भोजन योजना कार्बन स्कोर के साथ बनाता है।',
        'mod_ex_title':     'फिटनेस और व्यायाम योजनाकार',
        'mod_ex_desc':      'अपने आहार लक्ष्य से जुड़ी साप्ताहिक वर्कआउट योजना पाएं।',
        'mod_food_title':   'सामुदायिक फूड बैंक',
        'mod_food_desc':    'लाइव मैप पर जरूरतमंदों से अतिरिक्त भोजन जोड़ें।',
        'explore':          'अन्वेषण करें →',
        'sdg_title':        '🎯 6 UN टिकाऊ विकास लक्ष्यों का समर्थन',
        'cta_title':        'FeedForward के लिए तैयार हैं?',
        'cta_sub':          'हजारों लोगों के साथ एक स्वस्थ, टिकाऊ जीवन बनाएं।',
        'cta_btn':          '🌱 मुफ्त शुरू करें',

        # Dashboard
        'dash_morning':     'शुभ प्रभात',
        'dash_afternoon':   'शुभ दोपहर',
        'dash_evening':     'शुभ संध्या',
        'dash_subtitle':    'आज का आपका स्वास्थ्य सारांश',
        'dash_new_diet':    '🔄 नई आहार योजना',
        'dash_new_ex':      '🔄 नई व्यायाम योजना',
        'dash_streak':      'वर्कआउट स्ट्रीक',
        'dash_weight':      'वर्तमान वजन (kg)',
        'dash_cal':         'आज की कैलोरी',
        'dash_carbon':      'कार्बन स्कोर (kg CO₂)',
        'dash_meals_title': 'आज के भोजन',
        'dash_view_plan':   'पूरी योजना देखें →',
        'dash_workout':     'आज का वर्कआउट',
        'dash_rest_day':    '😴 आराम का दिन — रिकवरी जरूरी है!',
        'dash_food_title':  'आपके पास उपलब्ध खाना',
        'dash_view_map':    'मैप देखें →',
        'dash_log_title':   'आज की प्रगति दर्ज करें',
        'dash_no_plan':     'व्यक्तिगत योजनाएं पाने के लिए अपनी प्रोफाइल पूरी करें।',

        # Diet
        'diet_title':       '🥗 टिकाऊ आहार योजनाकार',
        'diet_sub':         'आपकी AI-निर्मित 7-दिन की कार्बन-जागरूक भोजन योजना',
        'diet_regen':       '🔄 योजना पुनः बनाएं',
        'diet_target_cal':  'लक्ष्य कैलोरी/दिन',
        'diet_avg_cal':     'औसत दैनिक कैलोरी',
        'diet_avg_carbon':  'औसत कार्बन (kg CO₂)',
        'diet_bmr':         'आपका BMR (kcal)',
        'diet_week_plan':   '📅 आपकी 7-दिन की भोजन योजना',
        'diet_breakfast':   'नाश्ता',
        'diet_lunch':       'दोपहर का खाना',
        'diet_dinner':      'रात का खाना',
        'diet_snack':       'स्नैक',
        'diet_swap_title':  '♻️ हरित विकल्प सुझाव',
        'diet_swap_sub':    'इन भोजनों में सबसे कम कार्बन फुटप्रिंट है:',
        'diet_no_plan':     'अभी कोई भोजन योजना नहीं',
        'diet_no_plan_sub': 'अपनी प्रोफाइल पूरी करें।',

        # Exercise
        'ex_title':         '💪 व्यायाम योजनाकार',
        'ex_sub':           'आपकी व्यक्तिगत साप्ताहिक वर्कआउट योजना',
        'ex_regen':         '🔄 योजना पुनः बनाएं',
        'ex_bmi_title':     '📊 आपका BMI',
        'ex_water_title':   '💧 दैनिक पानी लक्ष्य',
        'ex_week_plan':     '📅 आपकी साप्ताहिक वर्कआउट योजना',
        'ex_rest_day':      'आराम और रिकवरी दिन',
        'ex_rest_msg':      'आराम में मांसपेशियां बढ़ती हैं। पानी पीते रहें!',
        'ex_watch':         '▶ वीडियो देखें',
        'ex_no_plan':       'अभी कोई व्यायाम योजना नहीं',

        # Food Bank
        'fb_title':         '🤝 सामुदायिक फूड बैंक',
        'fb_sub':           'अतिरिक्त भोजन को जरूरतमंदों से जोड़ें — लाइव मैप',
        'fb_donate_btn':    '+ खाना दान करें',
        'fb_my_donations':  'मेरे दान',
        'fb_my_claims':     'मेरे क्लेम',
        'fb_map_title':     '🗺️ लाइव फूड मैप',
        'fb_listings':      '🍱 उपलब्ध खाद्य सूची',
        'fb_claim':         '🙌 खाना लें',
        'fb_your_donation': 'आपका दान',
        'fb_no_listings':   'अभी कोई खाद्य सूची नहीं',
        'fb_no_list_sub':   'पहले दान करें! बचाया गया हर खाना मायने रखता है।',
        'fb_donate_now':    'अभी खाना दान करें',

        # Progress
        'prog_title':       '📊 प्रगति ट्रैकर',
        'prog_streak':      'वर्कआउट स्ट्रीक',
        'prog_logs':        'कुल लॉग',
        'prog_weight':      'नवीनतम वजन',
        'prog_water':       'अंतिम पानी (L)',
        'prog_log_title':   '📝 आज की प्रगति दर्ज करें',
        'prog_weight_lbl':  'वजन (kg)',
        'prog_water_lbl':   'पानी पिया (लीटर)',
        'prog_cal_in':      'ली गई कैलोरी',
        'prog_cal_out':     'जलाई गई कैलोरी',
        'prog_mood':        'आज का मूड',
        'prog_workout':     'आज वर्कआउट किया ✅',
        'prog_notes':       'नोट्स (वैकल्पिक)',
        'prog_save':        '💾 प्रगति सेव करें',
        'prog_chart_wt':    '⚖️ वजन समय के साथ',
        'prog_chart_cal':   '🔥 कैलोरी अंदर बनाम बाहर',
        'prog_history':     '📅 लॉग इतिहास',
        'prog_date':        'तारीख',
        'prog_no_logs':     'अभी कोई लॉग नहीं। आज से शुरू करें!',

        # Profile setup
        'setup_title':      'अपनी प्रोफाइल सेट करें',
        'setup_sub':        'हम तुरंत आपकी व्यक्तिगत योजनाएं बनाएंगे',
        'setup_personal':   '👤 व्यक्तिगत जानकारी',
        'setup_diet':       '🥗 आहार प्राथमिकताएं',
        'setup_fitness':    '💪 फिटनेस जानकारी',
        'setup_generate':   '🚀 मेरी योजनाएं बनाएं →',
        'setup_age':        'उम्र (साल)',
        'setup_gender':     'लिंग',
        'setup_weight':     'वजन (kg)',
        'setup_height':     'ऊंचाई (cm)',
        'setup_location':   'आपका शहर / स्थान',
        'setup_diet_pref':  'आहार प्राथमिकता',
        'setup_goal':       'स्वास्थ्य लक्ष्य',
        'setup_level':      'फिटनेस स्तर',
        'setup_equipment':  'उपलब्ध उपकरण',
        'setup_days':       'व्यायाम दिन/सप्ताह',

        # Auth
        'login_title':      'वापस स्वागत है',
        'login_sub':        'अपने FeedForward खाते में लॉगिन करें',
        'login_email':      'ईमेल पता',
        'login_password':   'पासवर्ड',
        'login_btn':        'लॉगिन →',
        'login_no_acct':    'खाता नहीं है?',
        'login_register':   'यहाँ रजिस्टर करें',
        'reg_title':        'FeedForward से जुड़ें',
        'reg_sub':          'अपना मुफ्त खाता बनाएं',
        'reg_name':         'पूरा नाम',
        'reg_role':         'मैं जुड़ना चाहता हूं',
        'reg_btn':          'खाता बनाएं →',
        'reg_have_acct':    'पहले से खाता है?',

        # Footer
        'footer_tagline':   'समझदारी से खाएं। अच्छे से चलें। वापस दें।',
        'footer_built':     'Innovathon 2025 के लिए ❤️ से बनाया | Python + Flask',

        # Common
        'save':             'सेव करें',
        'cancel':           'रद्द करें',
        'delete':           'हटाएं',
        'edit':             'प्रोफाइल संपादित करें',
        'available':        'उपलब्ध',
        'claimed':          'लिया गया',
        'expired':          'समाप्त',
        'low_carbon':       'कम कार्बन ✅',
        'mood_great':       '😄 बहुत अच्छा',
        'mood_good':        '🙂 अच्छा',
        'mood_okay':        '😐 ठीक है',
        'mood_bad':         '😔 बुरा',
    }
}

# ── ALIAS KEYS — compatibility shims ───────────────────────────
# (Templates use these names; map to existing translation strings)
def get_translations(lang_code='en', lang=None):
    # Accept either positional or keyword argument
    code = lang_code if lang_code != 'en' or lang is None else lang
    base = TRANSLATIONS.get(code, TRANSLATIONS['en']).copy()
    # Hero aliases
    base.setdefault('hero_title',       base.get('hero_line1','FeedForward'))
    base.setdefault('hero_subtitle',    base.get('hero_sub',''))
    base.setdefault('hero_btn_start',   base.get('hero_cta','Get Started'))
    base.setdefault('hero_btn_donate',  base.get('hero_donate','Donate Food'))
    # Auth aliases
    base.setdefault('auth_welcome',     base.get('login_title','Welcome Back'))
    base.setdefault('auth_login_sub',   base.get('login_sub','Sign in to your account'))
    base.setdefault('auth_email',       base.get('login_email','Email'))
    base.setdefault('auth_password',    base.get('login_password','Password'))
    base.setdefault('auth_login_btn',   base.get('login_btn','Login'))
    base.setdefault('auth_no_acct',     base.get('login_no_acct','No account?'))
    base.setdefault('auth_register',    base.get('login_register','Register'))
    base.setdefault('auth_join',        base.get('reg_title','Join FeedForward'))
    base.setdefault('auth_name',        base.get('reg_name','Full Name'))
    base.setdefault('auth_create',      base.get('reg_btn','Create Account'))
    base.setdefault('auth_have_acct',   base.get('reg_have_acct','Already have an account?'))
    # Dashboard aliases
    base.setdefault('dash_meals',       base.get('dash_meals_title',"Today's Meals"))
    base.setdefault('dash_rest',        base.get('dash_rest_day','Rest Day'))
    base.setdefault('dash_nearby',      base.get('dash_food_title','Available Food Near You'))
    base.setdefault('dash_log',         base.get('dash_log_title',"Log Today's Progress"))
    base.setdefault('dash_save',        'Save Log')
    base.setdefault('dash_claim',       base.get('fb_claim','Claim Food'))
    base.setdefault('meal_snack',       'Snack')
    base.setdefault('prog_done',        'Done')
    base.setdefault('prog_water_l',     base.get('prog_water','Water (L)'))
    base.setdefault('prog_weight_kg',   base.get('prog_weight','Weight (kg)'))
    base.setdefault('regenerate',       'Regenerate')
    # Foodbank aliases
    base.setdefault('fb_available',     base.get('fb_listings','Available Food'))
    base.setdefault('fb_subtitle',      base.get('fb_sub','Connect surplus food with people in need'))
    base.setdefault('fb_donate',        base.get('fb_donate_btn','+ Donate Food'))
    base.setdefault('fb_post',          base.get('fb_donate_btn','Post Food'))
    base.setdefault('fb_map',           base.get('fb_map_title','Live Map'))
    base.setdefault('fb_claimed',       'Claimed')
    base.setdefault('fb_expired',       'Expired')
    # Diet aliases
    base.setdefault('diet_title',       base.get('dt_title','🥗 Diet Planner'))
    # Exercise aliases  
    base.setdefault('ex_title',         base.get('ex_plan_title','💪 Exercise Planner'))
    # SDG
    base.setdefault('sdg_title',        '🌍 Aligned with UN Sustainable Development Goals')
    base.setdefault('setup_subtitle',   'Help us personalise your experience')
    return base
