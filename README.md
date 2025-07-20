# birthday-ping

No more "oh crap I forgot!" moments, this Python script sends out auto-generated birthday wishes to your people, on time, every time. Whether you're busy, forgetful, or just lazy (no judgment), `birthday-ping` has your back.

## What it does

* Reads birthdays from a `.csv` file
* Picks a random birthday letter template
* Fills in the name and sends it via email
* Runs in seconds and saves you from being *that* person

## How it's laid out

```
birthday-ping/
├── birthdays.csv             # Your birthday squad list
├── letter_templates/         # Pre-written birthday letters (randomly picked)
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── main.py                   # The boss script
├── .env                      # Where you keep your secrets (email + password)
├── .gitignore                # So your secrets don’t get pushed accidentally
└── README.md                 # This doc you're reading
```

## 🛠 Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/birthday-ping.git
   cd birthday-ping
   ```

2. **Install dependencies**

   ```bash
   pip install pandas python-dotenv
   ```

3. **Create your `.env` file**

   Add your email details here (make sure 2FA is off or you're using an app password):

   ```env
   EMAIL=your_email@gmail.com
   PASSWORD=your_email_password
   ```

4. **Update the `birthdays.csv` file**

   Format:

   ```csv
   name,email,year,month,day
   John,john@example.com,1990,7,20
   Jane,jane@example.com,1992,12,5
   ```

5. **Run it**

   ```bash
   python main.py
   ```

   If it’s someone’s birthday today, boom email sent!

## To-Do (aka "stuff I might add later")

* Time zone support (for that one friend in Australia)
* Auto-run daily using cron or Windows Task Scheduler
* Maybe a basic web dashboard? We’ll see

---

**Made with love, Python, and caffeine by [LinkedIn](https://www.linkedin.com/in/nomadbeetle) · [GitHub](https://github.com/nomadbeetle)**
