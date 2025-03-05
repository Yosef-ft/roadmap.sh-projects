# Expense Tracker  

A simple expense tracker to manage your finances.  

## Overview  
A simple expense tracker application to manage your finances. The application allows users to add, delete, and view their expenses. The application is also able to provide a summary of the expenses.  


## Project structure
```bash
expense_tracker/
├── src/
│   ├── ExpenseTracker.php
│   └── Utils.php          
├── tests/
│   └── ExpenseTrackerTest.php
├── composer.json
├── phpunit.xml
└── vendor/ # run ./vendor/bin/phpunit --generate-configuration
```

## Getting Started

```bash
# install PhpUnit for unit test
composer require --dev phpunit/phpunit
./vendor/bin/phpunit --generate-configuration
# Ensure the autoloader is fresh
composer dump-autoload
# Run the tests
./vendor/bin/phpunit tests/
```
