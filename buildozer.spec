[app]
title = DroneVideoSearch
package.name = dronevideosearch
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.4
requirements = python3,kivy==2.3.0,telethon,pillow,cryptography,requests,yt-dlp
orientation = portrait
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 21
android.private_storage = False
android.archs = arm64-v8a
android.ndk = 25b

[buildozer]
log_level = 2
