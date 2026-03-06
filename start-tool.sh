#!/bin/bash
# Start Financial Tool Local Server

cd /home/shyanair/financial-tool

echo "═══════════════════════════════════════════════════════════"
echo "🚀 Starting Financial Tool..."
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "🌐 Opening in browser: http://localhost:8080"
echo ""
echo "✅ All features enabled (Car comparison, Charts, etc.)"
echo "🔒 Private - only accessible on YOUR computer"
echo ""
echo "Press Ctrl+C to stop the server"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Open browser automatically
if command -v firefox &> /dev/null; then
    firefox http://localhost:8080 &
elif command -v google-chrome &> /dev/null; then
    google-chrome http://localhost:8080 &
fi

# Start server
python3 -m http.server 8080
