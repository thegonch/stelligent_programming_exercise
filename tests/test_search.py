from __future__ import print_function  # Python 2/3 compatibility
from unittest import TestCase
from ..search_locality import get_args, parse_files

__author__ = "Stephen Goncher"
__copyright__ = "Copyright 2017, Stelligent Systems, LLC"


class SearchLocalityTestCase(TestCase):
    def setUp(cls):
        parser = get_args()
        cls.parser = parser


class RunTestCases(SearchLocalityTestCase):
    def test_with_empty_args(self):
        # Passing no args, should fail with error message about missing args
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

        # verify the same for the help menu, which is built into the parser
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['-h'])

    def test_with_minimal_args(self):
        # Single word terms
        args = self.parser.parse_args(['it', 'it'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['her', 'active'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['file1.txt'])

        # Phrases
        args = self.parser.parse_args(['hello there', 'nice to meet you'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['perfectly favourite', 'eat she'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['file2.txt'])

    def test_with_small_context(self):
        # Small context between singluar terms to see if we get back any files
        args = self.parser.parse_args(['it', 'it', '5', 'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['paid', 'love', '5', 'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['test_file1.txt', 'test_file2.txt'])

        # Small context test between phrases to see if we get back any files
        args = self.parser.parse_args(['how we doing', 'not so great', '5',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['no humoured', 'so comparison \
                                       inquietude', '5', 'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['test_file1.txt'])

    def test_with_large_context(self):
        # Larger context test between two singluar terms
        args = self.parser.parse_args(['Ultimate', 'neatness', '25',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['it', 'it', '25', 'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['test_file1.txt', 'test_file2.txt'])

        # Larger context test between two phrases
        args = self.parser.parse_args(['well hello', 'aw cool', '25',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['Colonel gravity get thought fat',
                                       'Am cottage calling', '25',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertTrue(result)
        self.assertEqual(result, ['test_file4.txt'])

    def test_ignore_non_text_files(self):
        args = self.parser.parse_args(['two', 'men'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['opinion', 'forbade', '5',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['bachelor but add',
                                       'pleasure doubtful sociable'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

        args = self.parser.parse_args(['opinion offered',
                                       'Friendly as stronger', '25',
                                       'more_tests'])
        result = parse_files(args.term_1.lower(), args.term_2.lower(),
                             args.context, args.dir_name)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
