from os import getenv

API_ID = int(getenv("API_ID", "16436100")) #optional
API_HASH = getenv("API_HASH", "4599e8f16f52517e608b719fa4665467") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "810227767"))
BOT_TOKEN = getenv("BOT_TOKEN", "5680740751:AAEyL7-IFs2xpemSNL6Y7-WWHzumibmKOns")
BOTLOG_CHATID = getenv("BOTLOG_CHATID")
REPO_URL = getenv("REPO_URL", "https://github.com/bitchlah/ALBY-Userbot")
BRANCH = getenv("BRANCH", "ALBY-Userbot") #don't change
STRING_SESSION = getenv("STRING_SESSION", "1BVtsOG0Bu3E9nfqVnFu2plh9kkfBO0aS-VKEBC74NQpExQfCa3DQ3G6LmH3FrkBPWLLE8tGeC_kfTTSgGsdhMnwaawpqWf9lIQRSunfp_3I10MQ6yrN7ejiSiy-7aW9xqviCYp4FhfgiS6KwDwZDxlqDqfi3jLHQrCviFuVRXLQuEma7ECyou6NLh3PmhjUfKQ2tjPyw3Vyra0sFc2m19H98UIGrQuZ2DdKHGWi0mPo117ndrIXuezMXqWou-zz3m3bwk0B23cGnTndHUwmspTP8J7Co3S43RIpJVfDX4K3wQNSBozMv6d5pAzbZUvWzKgCBAqd1oa6Ifc98a76Fdu2pPtS24f0=")
