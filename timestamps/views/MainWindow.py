# -*- coding: utf-8 -*-

import pendulum
import dateutil.relativedelta

from time import gmtime, strftime
from datetime import datetime

from PyQt5.QtCore import QTime, QDate
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUiType

from .AboutDialog import AboutDialog
from constants import *


Ui_MainWindow, MainWindow = loadUiType(PATH_VIEWS + "MainWindow.ui")


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.reset_forms_date_difference()
        self.set_triggers()

    def set_triggers(self):
        # Menubar actions
        self.ui.action_about.triggered.connect(self.show_about_dialog)
        self.ui.action_exit.triggered.connect(QApplication.quit)

        # Application actions
        self.ui.button_calculate.clicked.connect(self.get_calculation)
        self.ui.button_reset.clicked.connect(self.get_reset)

    def get_reset(self):
        """ Return reset method based on current tab index (switch) """
        return {
            0: lambda: self.reset_forms_week(),
            1: lambda: self.reset_forms_month(),
            2: lambda: self.reset_forms_date_difference(),
        }.get(self.ui.tabs.currentIndex())()

    def get_calculation(self):
        """ Return calculation method based on current tab index (switch) """
        return {
            0: lambda: self.calculate_timestamp_week(),
            1: lambda: self.calculate_timestamp_month(),
            2: lambda: self.calculate_date_difference(),
        }.get(self.ui.tabs.currentIndex())()

    def reset_forms_week(self):
        reset_time, reset_text = QTime(00, 00), "00:00"

        self.ui.form_week_1_time_start.setTime(reset_time)
        self.ui.form_week_2_time_start.setTime(reset_time)
        self.ui.form_week_3_time_start.setTime(reset_time)
        self.ui.form_week_4_time_start.setTime(reset_time)
        self.ui.form_week_5_time_start.setTime(reset_time)
        self.ui.form_week_6_time_start.setTime(reset_time)
        self.ui.form_week_7_time_start.setTime(reset_time)

        self.ui.form_week_1_time_end.setTime(reset_time)
        self.ui.form_week_2_time_end.setTime(reset_time)
        self.ui.form_week_3_time_end.setTime(reset_time)
        self.ui.form_week_4_time_end.setTime(reset_time)
        self.ui.form_week_5_time_end.setTime(reset_time)
        self.ui.form_week_6_time_end.setTime(reset_time)
        self.ui.form_week_7_time_end.setTime(reset_time)

        self.ui.form_week_1_results.setText(reset_text)
        self.ui.form_week_2_results.setText(reset_text)
        self.ui.form_week_3_results.setText(reset_text)
        self.ui.form_week_4_results.setText(reset_text)
        self.ui.form_week_5_results.setText(reset_text)
        self.ui.form_week_6_results.setText(reset_text)
        self.ui.form_week_7_results.setText(reset_text)

        self.ui.form_week_total_results.setText("00:00:00")

    def reset_forms_month(self):
        reset_time, reset_text = QTime(00, 00), "00:00"

        self.ui.form_month_1_time_start.setTime(reset_time)
        self.ui.form_month_2_time_start.setTime(reset_time)
        self.ui.form_month_3_time_start.setTime(reset_time)
        self.ui.form_month_4_time_start.setTime(reset_time)
        self.ui.form_month_5_time_start.setTime(reset_time)
        self.ui.form_month_6_time_start.setTime(reset_time)
        self.ui.form_month_7_time_start.setTime(reset_time)
        self.ui.form_month_8_time_start.setTime(reset_time)
        self.ui.form_month_9_time_start.setTime(reset_time)
        self.ui.form_month_10_time_start.setTime(reset_time)
        self.ui.form_month_11_time_start.setTime(reset_time)
        self.ui.form_month_12_time_start.setTime(reset_time)
        self.ui.form_month_13_time_start.setTime(reset_time)
        self.ui.form_month_14_time_start.setTime(reset_time)
        self.ui.form_month_15_time_start.setTime(reset_time)
        self.ui.form_month_16_time_start.setTime(reset_time)
        self.ui.form_month_17_time_start.setTime(reset_time)
        self.ui.form_month_18_time_start.setTime(reset_time)
        self.ui.form_month_19_time_start.setTime(reset_time)
        self.ui.form_month_20_time_start.setTime(reset_time)
        self.ui.form_month_21_time_start.setTime(reset_time)
        self.ui.form_month_22_time_start.setTime(reset_time)
        self.ui.form_month_23_time_start.setTime(reset_time)
        self.ui.form_month_24_time_start.setTime(reset_time)
        self.ui.form_month_25_time_start.setTime(reset_time)
        self.ui.form_month_26_time_start.setTime(reset_time)
        self.ui.form_month_27_time_start.setTime(reset_time)
        self.ui.form_month_28_time_start.setTime(reset_time)
        self.ui.form_month_29_time_start.setTime(reset_time)
        self.ui.form_month_30_time_start.setTime(reset_time)
        self.ui.form_month_31_time_start.setTime(reset_time)

        self.ui.form_month_1_time_end.setTime(reset_time)
        self.ui.form_month_2_time_end.setTime(reset_time)
        self.ui.form_month_3_time_end.setTime(reset_time)
        self.ui.form_month_4_time_end.setTime(reset_time)
        self.ui.form_month_5_time_end.setTime(reset_time)
        self.ui.form_month_6_time_end.setTime(reset_time)
        self.ui.form_month_7_time_end.setTime(reset_time)
        self.ui.form_month_8_time_end.setTime(reset_time)
        self.ui.form_month_9_time_end.setTime(reset_time)
        self.ui.form_month_10_time_end.setTime(reset_time)
        self.ui.form_month_11_time_end.setTime(reset_time)
        self.ui.form_month_12_time_end.setTime(reset_time)
        self.ui.form_month_13_time_end.setTime(reset_time)
        self.ui.form_month_14_time_end.setTime(reset_time)
        self.ui.form_month_15_time_end.setTime(reset_time)
        self.ui.form_month_16_time_end.setTime(reset_time)
        self.ui.form_month_17_time_end.setTime(reset_time)
        self.ui.form_month_18_time_end.setTime(reset_time)
        self.ui.form_month_19_time_end.setTime(reset_time)
        self.ui.form_month_20_time_end.setTime(reset_time)
        self.ui.form_month_21_time_end.setTime(reset_time)
        self.ui.form_month_22_time_end.setTime(reset_time)
        self.ui.form_month_23_time_end.setTime(reset_time)
        self.ui.form_month_24_time_end.setTime(reset_time)
        self.ui.form_month_25_time_end.setTime(reset_time)
        self.ui.form_month_26_time_end.setTime(reset_time)
        self.ui.form_month_27_time_end.setTime(reset_time)
        self.ui.form_month_28_time_end.setTime(reset_time)
        self.ui.form_month_29_time_end.setTime(reset_time)
        self.ui.form_month_30_time_end.setTime(reset_time)
        self.ui.form_month_31_time_end.setTime(reset_time)

        self.ui.form_month_total_results.setText(reset_text)

    def reset_forms_date_difference(self):
        reset_date, reset_text = QDate.currentDate(), "0"

        self.ui.form_date_difference_time_start.setDate(reset_date)
        self.ui.form_date_difference_time_end.setDate(reset_date)

        self.ui.result_date_difference_years.setText(reset_text)
        self.ui.result_date_difference_months.setText(reset_text)
        self.ui.result_date_difference_weeks.setText(reset_text)
        self.ui.result_date_difference_days.setText(reset_text)
        self.ui.result_date_difference_hours.setText(reset_text)
        self.ui.result_date_difference_minutes.setText(reset_text)
        self.ui.result_date_difference_seconds.setText(reset_text)

        self.ui.result_date_difference_human_years.setText(reset_text)
        self.ui.result_date_difference_human_months.setText(reset_text)
        self.ui.result_date_difference_human_days.setText(reset_text)
        self.ui.result_date_difference_human_hours.setText(reset_text)
        self.ui.result_date_difference_human_minutes.setText(reset_text)

    def calculate_timestamp_week(self):
        """ Update timestamps labels """

        # Timestamps
        timestamp = {
            1: str(self.get_datetime_difference(
                self.ui.form_week_1_time_start.time().toPyTime(),
                self.ui.form_week_1_time_end.time().toPyTime()
            )),
            2: str(self.get_datetime_difference(
                self.ui.form_week_2_time_start.time().toPyTime(),
                self.ui.form_week_2_time_end.time().toPyTime()
            )),
            3: str(self.get_datetime_difference(
                self.ui.form_week_3_time_start.time().toPyTime(),
                self.ui.form_week_3_time_end.time().toPyTime()
            )),
            4: str(self.get_datetime_difference(
                self.ui.form_week_4_time_start.time().toPyTime(),
                self.ui.form_week_4_time_end.time().toPyTime()
            )),
            5: str(self.get_datetime_difference(
                self.ui.form_week_5_time_start.time().toPyTime(),
                self.ui.form_week_5_time_end.time().toPyTime()
            )),
            6: str(self.get_datetime_difference(
                self.ui.form_week_6_time_end.time().toPyTime(),
                self.ui.form_week_6_time_start.time().toPyTime()
            )),
            7: str(self.get_datetime_difference(
                self.ui.form_week_7_time_start.time().toPyTime(),
                self.ui.form_week_7_time_end.time().toPyTime()
            ))
        }

        # List of hourly timestamps
        hours = []
        for time in timestamp:
            hours.append(timestamp[time])

        # Update labels
        self.ui.form_week_1_results.setText(timestamp[1][:-3])
        self.ui.form_week_2_results.setText(timestamp[2][:-3])
        self.ui.form_week_3_results.setText(timestamp[3][:-3])
        self.ui.form_week_4_results.setText(timestamp[4][:-3])
        self.ui.form_week_5_results.setText(timestamp[5][:-3])
        self.ui.form_week_6_results.setText(timestamp[6][:-3])
        self.ui.form_week_7_results.setText(timestamp[7][:-3])
        self.ui.form_week_total_results.setText(
            str(self.get_total_hours(hours)[:-3])
        )

    def calculate_timestamp_month(self):
        """ Update timestamps labels """

        # Collect timestamps
        timestamp = {
            1: str(self.get_datetime_difference(
                self.ui.form_month_1_time_start.time().toPyTime(),
                self.ui.form_month_1_time_end.time().toPyTime()
            )),
            2: str(self.get_datetime_difference(
                self.ui.form_month_2_time_start.time().toPyTime(),
                self.ui.form_month_2_time_end.time().toPyTime()
            )),
            3: str(self.get_datetime_difference(
                self.ui.form_month_3_time_start.time().toPyTime(),
                self.ui.form_month_3_time_end.time().toPyTime()
            )),
            4: str(self.get_datetime_difference(
                self.ui.form_month_4_time_start.time().toPyTime(),
                self.ui.form_month_4_time_end.time().toPyTime()
            )),
            5: str(self.get_datetime_difference(
                self.ui.form_month_5_time_start.time().toPyTime(),
                self.ui.form_month_5_time_end.time().toPyTime()
            )),
            6: str(self.get_datetime_difference(
                self.ui.form_month_6_time_start.time().toPyTime(),
                self.ui.form_month_6_time_end.time().toPyTime()
            )),
            7: str(self.get_datetime_difference(
                self.ui.form_month_7_time_start.time().toPyTime(),
                self.ui.form_month_7_time_end.time().toPyTime()
            )),
            8: str(self.get_datetime_difference(
                self.ui.form_month_8_time_start.time().toPyTime(),
                self.ui.form_month_8_time_end.time().toPyTime()
            )),
            9: str(self.get_datetime_difference(
                self.ui.form_month_9_time_start.time().toPyTime(),
                self.ui.form_month_9_time_end.time().toPyTime()
            )),
            10: str(self.get_datetime_difference(
                self.ui.form_month_10_time_start.time().toPyTime(),
                self.ui.form_month_10_time_end.time().toPyTime()
            )),
            11: str(self.get_datetime_difference(
                self.ui.form_month_11_time_start.time().toPyTime(),
                self.ui.form_month_11_time_end.time().toPyTime()
            )),
            12: str(self.get_datetime_difference(
                self.ui.form_month_12_time_start.time().toPyTime(),
                self.ui.form_month_12_time_end.time().toPyTime()
            )),
            13: str(self.get_datetime_difference(
                self.ui.form_month_13_time_start.time().toPyTime(),
                self.ui.form_month_13_time_end.time().toPyTime()
            )),
            14: str(self.get_datetime_difference(
                self.ui.form_month_14_time_start.time().toPyTime(),
                self.ui.form_month_14_time_end.time().toPyTime()
            )),
            15: str(self.get_datetime_difference(
                self.ui.form_month_15_time_start.time().toPyTime(),
                self.ui.form_month_15_time_end.time().toPyTime()
            )),
            16: str(self.get_datetime_difference(
                self.ui.form_month_16_time_start.time().toPyTime(),
                self.ui.form_month_16_time_end.time().toPyTime()
            )),
            17: str(self.get_datetime_difference(
                self.ui.form_month_17_time_start.time().toPyTime(),
                self.ui.form_month_17_time_end.time().toPyTime()
            )),
            18: str(self.get_datetime_difference(
                self.ui.form_month_18_time_start.time().toPyTime(),
                self.ui.form_month_18_time_end.time().toPyTime()
            )),
            19: str(self.get_datetime_difference(
                self.ui.form_month_19_time_start.time().toPyTime(),
                self.ui.form_month_19_time_end.time().toPyTime()
            )),
            20: str(self.get_datetime_difference(
                self.ui.form_month_20_time_start.time().toPyTime(),
                self.ui.form_month_20_time_end.time().toPyTime()
            )),
            21: str(self.get_datetime_difference(
                self.ui.form_month_21_time_start.time().toPyTime(),
                self.ui.form_month_21_time_end.time().toPyTime()
            )),
            22: str(self.get_datetime_difference(
                self.ui.form_month_22_time_start.time().toPyTime(),
                self.ui.form_month_22_time_end.time().toPyTime()
            )),
            23: str(self.get_datetime_difference(
                self.ui.form_month_23_time_start.time().toPyTime(),
                self.ui.form_month_23_time_end.time().toPyTime()
            )),
            24: str(self.get_datetime_difference(
                self.ui.form_month_24_time_start.time().toPyTime(),
                self.ui.form_month_24_time_end.time().toPyTime()
            )),
            25: str(self.get_datetime_difference(
                self.ui.form_month_25_time_start.time().toPyTime(),
                self.ui.form_month_25_time_end.time().toPyTime()
            )),
            26: str(self.get_datetime_difference(
                self.ui.form_month_26_time_start.time().toPyTime(),
                self.ui.form_month_26_time_end.time().toPyTime()
            )),
            27: str(self.get_datetime_difference(
                self.ui.form_month_27_time_start.time().toPyTime(),
                self.ui.form_month_27_time_end.time().toPyTime()
            )),
            28: str(self.get_datetime_difference(
                self.ui.form_month_28_time_start.time().toPyTime(),
                self.ui.form_month_28_time_end.time().toPyTime()
            )),
            29: str(self.get_datetime_difference(
                self.ui.form_month_29_time_start.time().toPyTime(),
                self.ui.form_month_29_time_end.time().toPyTime()
            )),
            30: str(self.get_datetime_difference(
                self.ui.form_month_30_time_start.time().toPyTime(),
                self.ui.form_month_30_time_end.time().toPyTime()
            )),
            31: str(self.get_datetime_difference(
                self.ui.form_month_31_time_start.time().toPyTime(),
                self.ui.form_month_31_time_end.time().toPyTime()
            ))
        }

        # List of hourly timestamps
        hours = []
        for time in timestamp:
            hours.append(timestamp[time])

        # Show the result to the user
        self.ui.form_month_total_results.setText(
            str(self.get_total_hours(hours))[:-3]
        )

    def calculate_date_difference(self):
        """ Update text labels with date difference """

        # Get input data
        input_start = self.ui.form_date_difference_time_start
        input_end = self.ui.form_date_difference_time_end
        qt_input_start = input_start.dateTime().toPyDateTime()
        qt_input_end = input_end.dateTime().toPyDateTime()

        # Check timezone
        timezone = self.get_timezone()

        # Get time difference
        time_start = pendulum.instance(qt_input_start, tz=timezone)
        time_end = pendulum.instance(qt_input_end, tz=timezone)
        time_difference = time_start.diff(time_end)
        human_time = self.human_readable_time(qt_input_start, qt_input_end)

        self.ui.result_date_difference_years.setText(
            str('{:n}'.format(int(time_difference.in_years())))
        )
        self.ui.result_date_difference_months.setText(
            str('{:n}'.format(int(time_difference.in_months())))
        )
        self.ui.result_date_difference_weeks.setText(
            str('{:n}'.format(int(time_difference.in_weeks())))
        )
        self.ui.result_date_difference_days.setText(
            str('{:n}'.format(int(time_difference.in_days())))
        )
        self.ui.result_date_difference_hours.setText(
            str('{:n}'.format(int(time_difference.in_hours())))
        )
        self.ui.result_date_difference_minutes.setText(
            str('{:n}'.format(int(time_difference.in_minutes())))
        )
        self.ui.result_date_difference_seconds.setText(
            str('{:n}'.format(int(time_difference.in_seconds())))
        )
        self.ui.result_date_difference_human_years.setText(
            str(human_time['years'])
        )
        self.ui.result_date_difference_human_months.setText(
            str(human_time['months'])
        )
        self.ui.result_date_difference_human_days.setText(
            str(human_time['days'])
        )
        self.ui.result_date_difference_human_hours.setText(
            str(human_time['hours'])
        )
        self.ui.result_date_difference_human_minutes.setText(
            str(human_time['minutes'])
        )

    @staticmethod
    def show_about_dialog():
        AboutDialog().exec_()

    @staticmethod
    def get_total_hours(hours):
        """ Return string of total hours """
        total_seconds = 0
        for hour in hours:
            time_split = [int(s) for s in hour.split(':')]
            total_seconds += (time_split[0] * 60 +
                              time_split[1]) * 60 + time_split[2]

        total_seconds, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(total_seconds, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    @staticmethod
    def get_datetime_difference(start, end, time_format='%H:%M:%S'):
        """ Return datetime difference """
        return "00:00:00" if start > end else (
            datetime.strptime(str(end), time_format) -
            datetime.strptime(str(start), time_format)
        )

    @staticmethod
    def get_timezone():
        """ Returns string of current timezone """
        timezone = strftime("%Z", gmtime())
        if timezone not in pendulum.timezones:
            return 'UTC'
        return timezone

    @staticmethod
    def human_readable_time(dt_start, dt_end):
        """ Takes two deltatime's and returns a dict """
        rd = dateutil.relativedelta.relativedelta(dt_end, dt_start)
        return {
            'years': rd.years,
            'months': rd.months,
            'days': rd.days,
            'hours': rd.hours,
            'minutes': rd.minutes
        }
