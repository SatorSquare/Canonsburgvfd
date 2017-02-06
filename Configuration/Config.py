import datetime

# This file exists as a place to store all constants dispersed throughout the controllers globally
# It serves as a settings file

# The name of our website
GLOBAL_TEMPLATE_VALUES = {
    "SITE_NAME" : 'Canonsburg Volunteer Fire Department - Canonsburg, Pennsylvania',
    
    "PHONE_RAW" : 7247461014, 
    "PHONE_READABLE" : '724-746-1014',
    
    "POLICE_PHONE_RAW" : 7247451801, 
    "POLICE_PHONE_READABLE" : '724-745-1801',
    
    "ADDRESS" : '1 Greenside Ave',
    "CITY" : 'Canonsburg',
    "STATE" : 'PA',
    "ZIP" : '15317',
    
    "YEAR" : datetime.datetime.now().year,
}

ROUTE_MAP = {
    '/' : 'pages_/home.html',
    '/FirePrevention': 'pages_/fire_prevention.html',
    '/JoinUs': 'pages_/join_us.html',
    '/Personnel': 'pages_/personnel.html',
    '/Apparatus': 'pages_/apparatus.html',
    '/History': 'pages_/history.html',
    '/Community': 'pages_/community.html',
    '/PhotoGallery': 'pages_/photo_gallery.html',
    '/ContactUs': 'pages_/contact_us.html'
}

GALLERY_PHOTOS_PER_PAGE = 40

