class Translation(object):
    START_TEXT = """Hi {} 😂,
I'm Lyra, your friendly and efficient URL uploader Assistant. 
If you have URLs to share, I'm here to help! Just send me the HTTP/HTTPS direct links, and I'll start uploading right away.
For more details on how to use my services, you can use the /help command.
I promise to handle your requests quickly and with care. Let's get started!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Download started in ** mode...**"
    UPLOAD_START = "Processing upload..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thank you <a href='https://t.me/TGTesla'>**꓄ꍟꌗ꒒ꍏ**</a> for helping us in this journey ❤️"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@TalismanBro"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>Site</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

Contact ADMIN if any error occurs @TalismanBro"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    LAZY_START_TEXT = """𝙷𝚎𝚕𝚕𝚘 {},

𝗬𝗼𝘂 𝗺𝘂𝘀𝘁 𝗯𝗲 𝗮 𝗩𝗲𝗿𝗶𝗳𝗶𝗲𝗱 𝗨𝘀𝗲𝗿 𝘁𝗼 𝘂𝘀𝗲 𝗺𝘆 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀.
The 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 has implemented verification to protect against spam and unauthorized usage, ensuring a secure and efficient experience for all users.

Please contact my Developer to become a verified user for free and unlock my full potential!
"""
    LAZY_DEVELOPER_TEXT = """▍║▍▏║ Hello Dear ADMIN 🌹 ║▍▏║▍
⭑┗┫⦀⦙ {} ⦙⦀┣┛⭑

 - Tell me what should i do for you.
 - or Just send me any url
"""
