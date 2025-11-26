{
    'name': 'Travelog Theme',
    'summary': 'XAPP Theme',
    'category': 'Theme',
    'version': '19.0.1.0',
    'author': 'XAPP',
    'depends': [
        'website',
        'theme_default',
        'travelog_packages',
        
    ],
    'data': [
        'views/theme_travelog_inherited.xml',
        'views/navbar.xml',
        'views/footer.xml',
        'views/homepage/sub_content.xml',
        'views/homepage/marque_text.xml',
        'views/homepage/single_card.xml',
        'views/homepage/s_live_package_text.xml',
        'views/homepage/featured_destination.xml',
        'views/homepage/featured_destination_header.xml',
        'views/homepage/s_package_booking.xml',
        'views/homepage/book_now_banner.xml',
        'views/homepage/package_banner.xml',
        'views/homepage/insights_banner.xml',
        'views/services/services_section.xml',
        'views/blog/blog_snippets.xml',
        'views/homepage/s_contact_us.xml',

        'views/homepage/hero.xml',
        'views/about/about_page.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            '/theme_travelog/static/src/scss/style.scss',
            '/theme_travelog/static/src/scss/navbar.scss',
            '/theme_travelog/static/src/scss/book_now_banner.scss',
            '/theme_travelog/static/src/scss/booking_success_modal.scss',
            '/theme_travelog/static/src/scss/blog_snippets.scss',
            '/theme_travelog/static/src/scss/insights_banner.scss',
            '/theme_travelog/static/src/scss/services_section.scss',
            '/theme_travelog/static/src/scss/about_page.scss',
            # '/theme_travelog/static/src/scss/hero_section.scss',

            '/theme_travelog/static/src/js/navbar.js',
            '/theme_travelog/static/src/js/book_now_banner.js',
            '/theme_travelog/static/src/js/booking_success_modal.js',
            '/theme_travelog/static/src/js/blog_snippets.js',
            '/theme_travelog/static/src/js/insights_banner.js',
            '/theme_travelog/static/src/js/services_section.js',
            '/theme_travelog/static/src/js/travelog_cards.js',
            '/theme_travelog/static/src/js/hero_section.js',
            '/theme_travelog/static/src/js/featured_destination.js',
            '/theme_travelog/static/src/js/package_booking.js',
            '/theme_travelog/static/src/js/about_page.js',
        ],
    },


    'images': [

        'static/description/theme_travelog_cover.jpg',

        'static/description/theme_travelog_screenshot.jpg',

    ],

    'license': 'LGPL-3',
    'application': True,
    'installable': True,
}
##############################################################################
