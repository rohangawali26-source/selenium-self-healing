# Selenium Self-Healing Framework (Experimental)

This is a small experimental project built while working with Selenium automation.
The main idea is to reduce test failures caused by minor UI changes, especially when
XPath locators break.

Instead of immediately failing a test, the framework tries to recover by finding
a similar element on the page and continuing execution.

This is **not a complete or production-ready solution**, but a learning-focused
attempt to handle a very common Selenium pain point.

---

## Why this project

While working with Selenium, I noticed that many tests fail due to small and frequent
UI changes like renamed IDs, updated classes, or slight DOM restructuring.
Maintaining locators becomes time-consuming.

This project explores a basic self-healing approach without using AI or external tools.

---

## How it works (high level)

1. Test tries to find an element using the stored XPath
2. If the locator fails, the healer logic is triggered
3. The page DOM is scanned for similar elements
4. A simple matching strategy (tag + visible text) is used
5. If a match is found, the test continues instead of failing

---

## Current scope & limitations

- Only supports XPath-based locators
- Healing logic is currently limited to buttons and inputs
- Matching is mostly text-based
- Dynamic and highly complex UIs may still fail

This is intentional to keep the project simple and understandable.

---

## Project structure

