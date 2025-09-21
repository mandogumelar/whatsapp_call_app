[app]

title = My WhatsApp Call App
package.name = whatsappcall
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.12,kivy
orientation = portrait
fullscreen = 0

# Android
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33
android.ndk_api = 21
android.accept_sdk_license = True

# Paths (WSL friendly)
android.sdk_path = /home/mando/.buildozer/android/platform/android-sdk
android.ndk_path = /home/mando/.buildozer/android/platform/android-ndk-r23b
android.ant_path = /home/mando/.buildozer/android/platform/apache-ant-1.9.4

# Debug / build
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
