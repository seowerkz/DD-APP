# Double D Distribution App

## Installation
 * Clone repository
 * Create virtualenv
 * Activate virtualenv
 * Create the database
  * `$ psql`
  * `# CREATE ROLE doubledadmin PASSWORD 'DXSxD81V';`
  * `# ALTER ROLE doubledadmin WITH LOGIN;`
  * `# CREATE DATABASE "doubled" OWNER "doubledadmin";`
  * `# \q`
 * `$ cd` into the project directory
 * `$ pip install -r requirements.txt`
 * `$ npm install`
 * `$ python manage.py migrate`
 * `$ python manage.py createsuperuser`
 * `$ python manage.py runserver`

## Grunt
 * `$ grunt watch` can be run to watch the app folders for changes to source files
 * Metronic Theme is not being watched, only project created files and files in `doubleddistributionapp/static/admin/less`

## Theme
[Admin4 from Metronic by Keenthemes](http://www.keenthemes.com/preview/metronic/theme/templates/admin4/)

## Permissions
 * Permissions are handled based on the group the user is in. Driver, Shop, and Office are all groups that a user can be in which limits their views in the app. Superusers will see all.