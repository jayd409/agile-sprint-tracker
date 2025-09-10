import numpy as np
import pandas as pd

def make_backlog(n=60):
    rng = np.random.default_rng(42)

    # E-commerce platform epics
    epics = [
        'Authentication & Identity',
        'Product Catalog',
        'Shopping Cart & Checkout',
        'Payment Processing',
        'Order Management',
        'User Account',
        'Admin Dashboard',
        'Search & Discovery',
        'Mobile Experience',
        'Performance & Infrastructure'
    ]

    # Realistic e-commerce user story titles
    titles = [
        'User Login with Email & Password',
        'Product Catalog Search by Category',
        'Shopping Cart Add/Remove Items',
        'Checkout with Credit Card',
        'Order History Page',
        'Admin Dashboard Overview',
        'Product Recommendations',
        'Implement Two-Factor Authentication',
        'Mobile App Push Notifications',
        'Payment Gateway Integration',
        'Inventory Management System',
        'User Profile & Address Book',
        'Product Reviews & Ratings',
        'Wishlist Feature',
        'Order Status Tracking',
        'Admin Analytics Dashboard',
        'Email Notification Service',
        'Database Performance Tuning',
        'Search Cache Layer',
        'Real-time Order Updates',
        'Guest Checkout Option',
        'Product Filter by Price',
        'Coupon & Discount System',
        'Admin User Management',
        'Payment Refund Processing',
        'SSL Certificate Management',
        'Product Image Optimization',
        'Mobile Responsive Design',
        'Customer Support Chat',
        'Bulk Order Processing',
        'Tax Calculation Engine',
        'Shipping Integration',
        'Return Request System',
        'Analytics Event Tracking',
        'API Rate Limiting',
        'Backup & Disaster Recovery',
        'CDN Integration',
        'Dark Mode UI',
        'Multi-language Support',
        'Accessibility Compliance',
        'Product Recommendations Engine',
        'Email Newsletter',
        'SMS Notifications',
        'Social Login Integration',
        'Fraud Detection System',
        'KYC Verification',
        'API Documentation',
        'Load Testing',
        'Security Audit',
        'Performance Monitoring',
        'Customer Segmentation',
        'A/B Testing Framework',
        'Admin Audit Logs',
        'Product Bulk Import',
        'Vendor Portal',
        'Promotional Banner System',
        'Gift Card Feature',
        'Subscription Management',
        'Dynamic Pricing Engine',
        'Inventory Alerts'
    ]

    # Business value: 5-13 (realistic range)
    business_value = rng.integers(5, 14, n)

    # MoSCoW distribution: 40% Must, 30% Should, 20% Could, 10% Won't
    moscow_vals = rng.choice(['Must Have', 'Should', 'Could', 'Won\'t'], n, p=[0.4, 0.3, 0.2, 0.1])

    # Story points: Fibonacci sequence 1-13
    fib_points = [1, 2, 3, 5, 8, 13]
    points = rng.choice(fib_points, n)

    # Time criticality: 1-10 scale
    time_criticality = rng.integers(1, 11, n)

    # Risk reduction: 1-10 scale
    risk_reduction = rng.integers(1, 11, n)

    df = pd.DataFrame({
        'story_id': [f'US-{i:03d}' for i in range(1, n+1)],
        'epic': rng.choice(epics, n),
        'title': rng.choice(titles, n),
        'moscow': moscow_vals,
        'points': points,
        'business_value': business_value,
        'time_criticality': time_criticality,
        'risk_reduction': risk_reduction,
        'depends_on': [
            f'US-{max(1, i-rng.integers(1, 4)):03d}' if rng.random() < 0.2 else None
            for i in range(1, n+1)
        ]
    })

    return df
