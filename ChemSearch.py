# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ChemSearch.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 11/20/22 23:12
"""
import re
import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    """
    get html from a url
    :param url: url
    :return: html
    """
    # get html from url
    response = requests.get(url)
    # parse html
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


class ChemSearch:
    """
    from a product code or CAS number, find the name of the chemical
    """

    def __init__(self, number: str):
        self.chemical_name = None
        match = re.match(r'(\d+-\d+-\d+)', number)
        if match is None:
            self.type = 'code'
            self.code_search(number)
        else:
            self.type = 'cas'
            self.cas_search(number)

    def code_search(self, code: str):
        """
        search by product code
        :param code: product code
        :return: chemical name
        """
        html_parsed = get_html(f'https://www.msds.com/Msds/Search?q={code}')
        print(html_parsed.find_all('h4')[1].text.strip())

    def cas_search(self, cas: str):
        """
        search by CAS number
        :param cas: CAS number
        :return: chemical name
        """
        html_parsed = get_html(f'https://commonchemistry.cas.org/detail?cas_rn={cas}')
        if "Get detail failed: Detail not found" in html_parsed:
            html_parsed_alt = get_html(f'https://pubchem.ncbi.nlm.nih.gov/compound/{cas}')
            if html_parsed_alt.h1 is not None:
                return html_parsed_alt.h1.text
        if html_parsed.h1 is not None:
            return html_parsed.h1.text



ChemSearch('t2663')
