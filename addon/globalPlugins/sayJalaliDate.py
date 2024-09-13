# Example of localization

import addonHandler
import globalPluginHandler
import os
import sys
import ui
from scriptHandler import script
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)
import jdatetime

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(gesture="kb:NVDA+shift+control+f12")
	def script_sayDate(self, gesture):
		now = jdatetime.datetime.now()
		months = (_("فروردین"), _("اردیبهشت"), _("خرداد"), _("تیر"), _("مرداد"), _("شهریور"), _("مهر"), _("آبان"), _("آذر"), _("دی"), _("بهمن"), _("اسفند"))
		weekdays = (_("شنبه"), _("یکشنبه"), _("دوشنبه"), _("سهشنبه"), _("چهارشنبه"), _("پنجشنبه"), _("جمعه"))
		# Translators: the comma sign between weekday name and the rest
		separator = _(",")
		ui.message(f"{weekdays[now.weekday()]}{separator} {now.day} {months[now.month-1]} {now.year}")