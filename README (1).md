# Password Strength Checker

A Python tool that rates password strength, explains exactly how to improve
a weak password, and estimates how long brute force would take to crack it.

## How to run

```
python password_checker.py
```

Type a password when asked (it stays hidden like a real login prompt).

## What I learned

- How attackers crack passwords: common-password lists first, brute force second
- Password entropy: why length beats complexity
- `getpass` for hidden input — passwords should never echo on screen
- Why everything runs locally: a strength checker must never send your
  password anywhere

## Note

Test with passwords you *don't* actually use — never type a real password
into any tool you don't fully trust, including this one.
