from BugBusters.data.constants import Constants

def test_login_flow(app):
    app.auth.open_login_form()
    app.auth.login(Constants.EMAIL, Constants.PASSWORD)
    app.page.wait_for_load_state("networkidle")
    app.auth.should_be_link_to_profile()