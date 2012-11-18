django-crowdsourcing
====================
This fork adds some additional features and bugfixes to django-crowdsourcing.

[upstream](http://code.google.com/p/django-crowdsourcing/) on Google Code

[documentation](http://packages.python.org/django-crowdsourcing/)


Date Option
-----------
An *Option* type for Dates has been added, with a sample frontend implementation using [bootstrap-datepicker](https://github.com/eternicode/bootstrap-datepicker)

Ranked Questions
----------------
An *Option* type for Ranked Questions has been added, allowing the participant to rank answers 1st, 2nd and 3rd. Useful for polling a participants order of preference.

Sections
--------
Questions now have optional Sections. Example usage in a template: [embeded_survey_questions.html](https://github.com/squidsoup/django-crowdsourcing/blob/master/example_app/templates/crowdsourcing/embeded_survey_questions.html)

Per Survey Scripts
------------------
Surveys now have an "Has script" flag which will render a script tag based on the slug name.
