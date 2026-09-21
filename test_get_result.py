import pytest

from get_result import get_result


@pytest.mark.parametrize(
    ("score", "attendance", "expected"),
    [
        # Допустимые классы и результаты.
        (0, 0, "Незачёт"),
        (49, 100, "Незачёт"),
        (50, 60, "Зачёт"),
        (69, 100, "Зачёт"),
        (70, 70, "Хорошо"),
        (89, 100, "Хорошо"),
        (90, 80, "Отлично"),
        (100, 100, "Отлично"),
        # Границы посещаемости и условия перехода между результатами.
        (90, 79, "Хорошо"),
        (70, 69, "Зачёт"),
        (50, 59, "Незачёт"),
        (50, 0, "Незачёт"),
        (100, 59, "Незачёт"),
    ],
)
def test_result_for_valid_equivalence_classes_and_boundaries(score, attendance, expected):
    assert get_result(score, attendance) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_invalid_score_boundaries(score):
    assert get_result(score, 50) == "Некорректный балл"


@pytest.mark.parametrize("attendance", [-1, 101])
def test_invalid_attendance_boundaries(attendance):
    assert get_result(50, attendance) == "Некорректная посещаемость"


@pytest.mark.parametrize("score", ["90", None, [90]])
def test_invalid_score_type(score):
    with pytest.raises(TypeError, match="Баллы должны быть числом"):
        get_result(score, 80)


@pytest.mark.parametrize("attendance", ["80", None, {80}])
def test_invalid_attendance_type(attendance):
    with pytest.raises(TypeError, match="Посещаемость должна быть числом"):
        get_result(90, attendance)
