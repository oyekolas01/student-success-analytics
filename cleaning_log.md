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

## date_unregistration
- Anomaly: 9 students have final_result = 'Fail' but also an unregistration date.
  8 of the 9 unregistered at day 0 or earlier (before the module began);
  1 unregistered at day 166 of 268. All 9 are 2013J.
- Cause: unknown. Not investigated yet.
- Decision: keep final_result as the official outcome. Flag these 9 rows.
  Open question: check whether they have any submissions or VLE clicks.

## imd_band
- Pattern: 90% of the missing values are in North Region (731) and Ireland (266).
  Hypothesis: IMD is an English index, so Ireland students would have none.
  North Region is unexplained.
- Missingness is NOT random: '?' students have higher Pass (47.8% vs 37.9%)
  and lower Withdrawn (21.2% vs 31.2%) than all students.
- Consequence: dropping them would bias the equity analysis.
  Report 'Unknown' as its own group.
- Possible confounder: the '?' group has more highly educated students
  (Postgraduate 11.4% vs 0.6%; HE Qualification 25.7% vs 14.1%).
  Module mix does NOT explain the gap (checked by module).
  Not yet tested: pass rate within each education level (stratified comparison).
- Do not interpret the higher pass rate of '?' students as an effect of location.