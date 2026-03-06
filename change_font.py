#!/usr/bin/env python3
"""
Change font from IBM Plex Mono to a more standard, readable font
Using system fonts that are widely available and easier to read
"""

print("🔤 Changing font to more readable standard font...")

with open('index.html', 'r') as f:
    html = f.read()

# Replace IBM Plex Mono with standard system fonts
# For body text: Use -apple-system (SF Pro on Mac), Segoe UI (Windows), Roboto (Android), Arial (fallback)
# For monospace numbers: Use SF Mono, Consolas, Monaco (better than IBM Plex Mono)

# Replace the main font-family in body
old_body_font = "font-family: 'IBM Plex Mono', 'Courier New', monospace;"
new_body_font = "font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;"

html = html.replace(old_body_font, new_body_font)

# Replace all inline IBM Plex Mono references with the new monospace stack
# For numbers and code, use a more readable monospace font
old_mono = "'IBM Plex Mono',monospace"
new_mono = "'SF Mono', 'Consolas', 'Monaco', 'Courier New', monospace"

html = html.replace(old_mono, new_mono)

old_mono2 = "'IBM Plex Mono', monospace"
html = html.replace(old_mono2, new_mono)

# Also update any font-family:'IBM Plex Mono' without quotes
old_mono3 = "font-family:IBM Plex Mono"
new_mono3 = "font-family:'SF Mono', Consolas, Monaco"
html = html.replace(old_mono3, new_mono3)

print("✅ Changed main body font to system font stack (SF Pro / Segoe UI / Roboto)")
print("✅ Changed monospace font to SF Mono / Consolas / Monaco")

# Write output
with open('index.html', 'w') as f:
    f.write(html)

print("=" * 60)
print("✅ FONT CHANGED TO MORE READABLE OPTIONS!")
print("")
print("📖 NEW FONTS:")
print("   • Body Text: System fonts (SF Pro on Mac, Segoe UI on Windows, Roboto on Android)")
print("   • Numbers/Code: SF Mono, Consolas, Monaco (easier to read than IBM Plex Mono)")
print("")
print("💡 BENEFITS:")
print("   ✅ Much easier to read")
print("   ✅ Native system fonts (no loading delay)")
print("   ✅ Familiar to users on each platform")
print("   ✅ Better clarity for long reading")
print("")
print("🎯 REFRESH YOUR BROWSER to see the new fonts!")
