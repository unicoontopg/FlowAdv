# static.py

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Flow</title>
    <link rel="icon" href="https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f4fd.svg" type="image/svg+xml">
    <style>
        * { box-sizing: border-box; }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-size: 2.2vh;
            font-family: 'Open Sans', Arial, sans-serif;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            overflow-y: auto;
            transition: background-color 0.3s, color 0.3s;
        }
        body.light {
            background: #f7f7f7;
            color: #333;
        }
        body.dark {
            background: #121212;
            color: white;
        }
        #addon {
            background: rgba(0, 0, 0, 0.8);
            padding: 1.5vh;
            border-radius: 10px;
            width: 65vh;
            max-width: 100%;
            text-align: center;
            margin-top: 10vh;
            transition: background 0.3s;
        }
        body.light #addon {
            background: rgba(255, 255, 255, 0.8);
        }
        .theme-toggle {
            position: absolute;
            top: 2vh;
            right: 2vh;
            cursor: pointer;
            font-size: 3vh;
        }
        .provider-group {
            margin-bottom: 2vh;
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5vh;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        body.light .provider-group {
            background: rgba(0, 0, 0, 0.1);
        }
        .provider-group label {
            flex-grow: 1;
            font-size: 2.2vh;
            text-align: left;
        }
        .provider-group input[type="checkbox"] {
            margin-right: 1vh;
            width: 4vh;
            height: 4vh;
        }
        button {
            border: 0;
            outline: 0;
            color: white;
            background: #8A5AAB;
            padding: 1.2vh 3.5vh;
            font-size: 2.2vh;
            font-weight: 600;
            cursor: pointer;
            width: 80%;
            max-width: 35vh;
            margin: 1vh auto;
            transition: box-shadow 0.1s ease-in-out;
        }
        button:hover {
            box-shadow: 0 0 1vh rgba(0, 0, 0, 0.2);
        }
        button:active {
            box-shadow: 0 0 0 0.5vh white inset;
        }
        #manifestBox {
            margin-top: 2vh;
            padding: 2vh;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            display: none;
            white-space: pre-wrap;
        }
    </style>
</head>
<body class="light">
    <div class="theme-toggle" id="themeToggle">🌙</div>
    <div id="addon">
        <h1>Flow</h1>
        <p>Seleziona i provider per generare il manifest:</p>
        <form id="provider-form">
            <div class="provider-group">
                <label for="streamingcommunity">
                    <input type="checkbox" id="streamingcommunity"> StreamingCommunity
                </label>
            </div>
            <div class="provider-group">
                <label for="lordchannel">
                    <input type="checkbox" id="lordchannel"> LordChannel
                </label>
            </div>
            <div class="provider-group">
                <label for="streamingwatch">
                    <input type="checkbox" id="streamingwatch"> StreamingWatch
                </label>
            </div>
        </form>
        <button id="generateManifestButton">Genera Manifest</button>
        <div id="manifestBox"></div>
    </div>
    <script>
        // Toggle Light/Dark Mode
        const themeToggle = document.getElementById('themeToggle');
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark');
            document.body.classList.toggle('light');
            themeToggle.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
        });

        // Function to generate the manifest
        function generateManifest() {
            let manifest = "|";
            const providers = {
                "streamingcommunity": "SC",
                "lordchannel": "LC",
                "streamingwatch": "SW"
            };

            // Check selected providers
            for (const id in providers) {
                if (document.getElementById(id).checked) {
                    manifest += providers[id] + "|";
                }
            }

            const instanceUrl = "https://flow-3qre.onrender.com/"; 
            const manifestUrl = `${instanceUrl}/${manifest}/manifest.json`;
            return manifestUrl;
        }

        // Display generated manifest
        document.getElementById('generateManifestButton').addEventListener('click', () => {
            const manifestUrl = generateManifest();
            const manifestBox = document.getElementById("manifestBox");
            manifestBox.style.display = "block";
            manifestBox.innerText = manifestUrl;
        });
    </script>
</body>
</html>
"""