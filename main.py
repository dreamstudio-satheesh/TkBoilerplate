#!/usr/bin/env python3
# Application entry point
from views.login_view import display_login
from views.dashboard_view import display_dashboard

def main():
    """Main application entry point."""
    display_login()
    # Add your main application logic here

if __name__ == "__main__":
    main()
