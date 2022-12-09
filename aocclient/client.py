import datetime
import logging
import os
import pathlib
import re

from bs4 import BeautifulSoup

from aocclient import http

LOG = logging.getLogger(__name__)
# Work for Linux
SESSION_FILE = f'{pathlib.Path.home()}/.cache/aoc_session_cookie'


class Client(http.HTTPClient):
    """Client for Advent of Code (AoC)"""

    def __init__(self, year=None, day=None, **kwargs):
        """Initialize a new client for the Advent of Code"""
        # If not year input, use current year
        year = year or datetime.date.today().year
        if not (year >= 2015 and 1 <= day <= 25):
            LOG.exception('Invalid year or day')
        self.year = year
        self.day = day
        endpoint = f'https://adventofcode.com/{self.year}/'
        super(Client, self).__init__(endpoint, **kwargs)
        self.get_session()

    def get_session(self):
        # Load cookie from file, you have to store your
        # session cookie manually.
        if not os.path.isfile(SESSION_FILE):
            LOG.exception(f'Session file {SESSION_FILE} is not found')
        with open(SESSION_FILE) as f:
            session = f.read().rstrip()
            self.session.cookies.set('session', session)

    def _validate_resp(self, resp):
        if resp.status_code != 200:
            LOG.exception(f'Response: {resp.status_code}')

        if 'please identify yourself' in resp.text.lower():
            LOG.exception(
                'Server return 200, but is asking for identification')

    def get_calendar(self):
        r = self.get('')
        self._validate_resp(r)
        # Extract calendar
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.find("pre", {"class": "calendar"}).prettify()

    def setup(self, input_fname=None):
        # Create README
        self.create_readme()

        # Get input
        if not input_fname:
            input_fname = "input.txt"
        input_fname = os.path.join(input_fname)
        self.get_input(input_fname)

    def create_readme(self):
        """Create a README, simple clone puzzle description,
        ugly but it works"""
        r = self.get('day/{self.day}')
        self._validate_resp(r)
        content = ''
        # Extract desc
        soup = BeautifulSoup(r.text, 'html.parser')
        # Get both part one and two
        result = soup.find_all("article", {"class": "day-desc"})
        for r in result:
            content += r.prettify()

        with open('README.md', 'w') as f:
            f.write(content)

    def get_input(self, fname):
        """Get puzzle input"""
        LOG.info(f'Getting input for day {self.day}')
        if os.path.isfile(fname):
            LOG.warn('Input file is existed, skip')
            return
        r = self.get('day/{self.day}/input')
        self._validate_resp(r)
        with open(fname, 'wb') as f:
            f.write(r.content)
        LOG.debug(f'Save input to file {fname}')

    def submit_answer(self, part, answer):
        LOG.info(f'Submitting day {self.day:02d} - part {part:02d}: {answer}')
        r = self.post('day/{self.day}/answer',
                      data={'level': part, 'answer': answer})
        self._validate_resp(r)

        t = r.text.lower()

        if 'did you already complete it' in t:
            LOG.warn('You already completed or wrong day/part')
            return True

        if "that's the right answer" in t:
            LOG.info('You got the right answer!')
            # TODO(kiennt26): Check if you finished?
            return True

        if 'you have to wait' in t:
            matches = re.compile(r'you have ([\w ]+) left to wait').findall(t)
            if matches:
                LOG.warn(f'You submitted too fast, {matches[0]} left to wait')
            else:
                LOG.warn('You submitted too fast, just slow down')

            return False

        LOG.warn('You submitted a wrong answer, try again')
        return False
