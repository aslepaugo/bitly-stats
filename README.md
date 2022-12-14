# BitLy Shortener and Stats tool

My BitLy helps to manage bitlinks and preview basic stats for it:

1. Create shortened link
2. Preview Link clicks stats

## First Time preparations

To successfully run your own BitLy comand tool you need

1. Create or use your BitLy account
2. Get BitLy API Token
3. Create file .env
4. Put your API Token there.

It should look like:

```bash
BYTLY_TOKEN=YOUR_API_ACCESS_TOKEN_HERE
```

5. Install requirements (Python 3 should be installed):

*Also, it's recommended to use virtual environment*

```bash
python -m venv venv
. ./venv/bin/activate
# or for Windows
# . .\venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

6. Run and Enjoy!

You can short your link

```bash
python my_bitly.py https://example.com
```

or you can review stats for already shortened link

```bash
python my_bitly.py  https://bit.ly/3eoOzle
```
