# Cleaning log

Every change made to the raw data, with the reason.

## studentAssessment.score
- Found: 173 values stored as '?' (text), which made the whole column text.
- Evidence: these rows all have a submission date, so the student did submit.
- Decision: convert '?' to missing (NaN). Do not use 0. Keep the rows.

## assessments.date
- Found: 11 values stored as '?', all of them Exams.
- Source: OULAD documentation says a missing exam date is the end of the last presentation week.
- Decision: convert '?' to missing, then fill from courses.module_presentation_length.
  Add a flag column date_is_imputed. (Assumption, to be verified.)