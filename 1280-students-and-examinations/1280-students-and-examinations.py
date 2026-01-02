import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subjects=students.merge(subjects,how='cross')
    exam_counts=(
        examinations
        .groupby(['student_id','subject_name'])
        .size()
        .reset_index(name='attended_exams')
    )
    result=(
        student_subjects
        .merge(exam_counts, on = ['student_id','subject_name'],how='left')
        .fillna({'attended_exams': 0})
    )
    return result.sort_values(['student_id','subject_name'])