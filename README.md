# bud-get

An automated budget the way I like it.

## Budgeting apps suck

I've used many banking and budget apps over the years and they always
disappointed in some way. They were either too simple or too complex. The common
main issue was importing transactions only worked sometimes, requiring me to
enter the data manually.

Years later, I discovered that I don't need to rely on a banking app. The best
and cheapest way to do budgets is a spreadsheet. That way, you can make your
budget exactly the way you like it.

## Just use a Spreadsheet!

Well, almost. The only drawback is the data entry aspect. Even if a bank lets
you download transactions as a CSV file, you still have to edit it and get it
into the right place.

This is were Bud-Get comes in! It automates creating and updating a budget
spreadsheet from CSV transaction reports.

## Such Automation

Download all your transactions, e.g. checking account, credit card, PayPal,
etc., as .CSV files into the inputs folder. Running Bud-Get will grab your
exported CSV and:

- categorize each transaction they way you like it
- format them into an income/expense table for each month
- generate a year-to-date overview
- add a pre-filled budget template based on your categories and downloaded data
- NOT send data anywhere for monetization, woohoo!

For now, Bud-Get only handles Numbers spreadsheets. While I like Excel, I don't
want to pay a subscription for it.

Dev notes:

- use [numbers-parser](https://github.com/masaccio/numbers-parser) to write to
  Numbers
