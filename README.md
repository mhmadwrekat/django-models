# django-models

---
***[Pull Request .....](https://github.com/mhmadwrekat/django-models/pull/1)***

---
## Feature Tasks and Requirements

1. Model
- [x] create snack_tracker_project project .
- [x] create snacks app .
- [x] Add snacks app to project .
- [x] create Snack model .
    - make sure it extends from proper base class .
    - add name as a CharField with maximum length of 64 characters .
    - add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option .
      - from django.contrib.auth import get_user_model .
    - add description TextField .
- [x] add model to admin .
- [x] modify Snack model have user friendly display in admin .
- [x] create migrations and migrate data .
- [x] create a super user .
- [x] run development server .
- [x] Add a few snacks via Admin panel .
- [x] create another user and more snacks via Admin panel .
- [x] confirm that snacks behave as expected with proper name, purchaser and description . 

2. Views for Snacks App
- [x] Dig around and see if there’s a sensible spot .
- [x] create SnackListView
    - extend ListView .
    - give a template of snack_list.html .
    - associate Snack model .
- [x] update url patterns for project .
    - empty path should include snacks.urls .
- [x] update snacks app urls .
    - empty sub-path should be handled by SnackListView .
        - Don’t forget to use as_view () .
- [x] add detail view .
    - link snack_detail.html template .
    - associate Snack model .
- [x] update app urlpatterns to handle detail view .
    - account for primary key in url .
    - path would look like localhost:8000/1/ to get to snack with id of 1 .

3. Templates
- [x] Addtemplates folder in root of project .
    - register templates folder in project settings TEMPLATES section .
- [x] create base.html ancestor template .
    - add main html document .
    - use Django Templating Language to allow child templates to insert content .
- [x] create snack_list.html template .
    - extend base template .
    - use Django Templating Language to display each snack’s name .
- [x] view home page (aka snack_list) and confirm snacks showing properly .
- [x] create snack_detail.html template .
    - template should extend base .
    - content should display snack’s name, description and purchaser .
- [x] add link in snack_list template to related detail page for each snack .
- [x] Add a link back to Home (aka snack_list) page from detail page .

4. User Acceptance Tests
- [x] Test Snack pages .
    - verify status code .
    - verify correct template use .
    - use url name instead of hard coded path .

---
