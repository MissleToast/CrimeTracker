# Define your monitoring area
boundary = {
    'min_lat': 32.7400,
    'max_lat': 32.7600,
    'min_lon': -97.3400,
    'max_lon': -97.3200
}

# Initialize tracker
tracker = CrimeTracker("Your Area Name", boundary)

# Add incidents
tracker.add_incident('INC001', 'Theft', 32.7450, -97.3300,
                     '2025-12-30 14:30:00', 'Medium')

# Analyze data
stats = tracker.get_statistics()
hotspots = tracker.get_hotspots()