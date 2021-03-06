# -*- encoding: utf-8 -*-
"""Implements different locators for UI"""

from selenium.webdriver.common.by import By
from .model import LocatorDict

action_locators = LocatorDict({
    "actions.menu": (
        By.LINK_TEXT, ("Actions")
    ),
    "actions.title": (
        By.XPATH, ("//h1[contains(@class, 'page-title')]/span")
    ),
    "actions.filter.invisible": (
        By.XPATH, ("//div[contains(@class, 'action-filters')]")
    ),
    "actions.pie.desc": (
        By.XPATH, ("//div[contains(@class, 'col-sm-offset-1')]/p[1]/span")
    ),
    "actions.desc.count": (
        By.XPATH, ("//div[contains(@class, 'col-sm-offset-1')]/p[2]/strong")
    ),
    "actions.pie.count": (
        By.XPATH, ("//div[@class='content']/span[@class='num']")
    ),
    "actions.filter": (
        By.LINK_TEXT, ("FILTER")
    ),
    "actions.filter.all": (
        By.ID, ("rha-multibutton-severityFiltersAll")
    ),
    "actions.filter.info": (
        By.ID, ("rha-multibutton-severityFiltersINFO")
    ),
    "actions.filter.warn": (
        By.ID, ("rha-multibutton-severityFiltersWARN")
    ),
    "actions.filter.error": (
        By.ID, ("rha-multibutton-severityFiltersERROR")
    ),
    "actions.downloadcsv": (
        By.XPATH, ("//div[@class='action']")
    ),
    "actions.section":(
        By.XPATH, ("//div[@class='tbody-scrollable']/table/tbody/tr")
    ),
    "actions.section.names":(
        By.XPATH, ("//div[@class='tbody-scrollable']/table/tbody/tr/td[1]")
    ),
    "actions.section.title": (
        By.XPATH, ("//div[contains(@class,'col-xs-12')]/h1")
    ),
    "actions.section.table": (
        By.ID, ("rha-actions-table")
    ),
    "actions.section.firstrow": (
    By.XPATH, ("//tr[@class='legend-item']")
    ),
    "actions.impacted.systemfirst": (
        By.XPATH, ("//table[@id='rha-actions-rule-table']/tbody/tr")
    ),
    "actions.system.hostname":(
        By.XPATH, ("//table[@id='rha-actions-rule-table']/tbody/tr/td[2]/a")

    ),
    "actions.system.modal.hostname": (
        By.XPATH, ("//div[@class='modal-title']/h2/div/span")
    ),
    "actions.system.close": (
        By.CSS_SELECTOR, ("div[ng-click='close()']")
    )
})
