# static.py

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Flow</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
        }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-size: 16px;
            font-family: 'Poppins', Arial, sans-serif;
            background-color: #1a1a1a;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow-y: auto;
        }

        #addon {
            background: rgba(0, 0, 0, 0.85);
            padding: 20px;
            border-radius: 15px;
            width: 90%;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
        }

        h1 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 10px;
        }

        h2 {
            font-size: 14px;
            font-weight: 400;
            font-style: italic;
            margin-bottom: 20px;
            color: #ccc;
        }

        .description {
            font-size: 14px;
            margin-bottom: 20px;
        }

        .provider-group {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
            background: linear-gradient(90deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
            padding: 10px;
            border-radius: 8px;
            transition: transform 0.2s;
        }

        .provider-group:hover {
            transform: scale(1.05);
        }

        .provider-label {
            font-size: 16px;
            font-weight: 400;
            color: white;
            text-align: left;
            flex-grow: 1;
        }

        .provider-group input[type="checkbox"] {
            width: 20px;
            height: 20px;
            margin-right: 10px;
            accent-color: #f09433;
        }

        button {
            border: none;
            outline: none;
            background: #6c63ff;
            color: white;
            padding: 12px 20px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
            transition: background 0.3s;
        }

        button:hover {
            background: #574bff;
        }

        .toggle-mode {
            position: absolute;
            top: 20px;
            right: 20px;
            background: transparent;
            border: 2px solid white;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
        }

        .toggle-mode:hover {
            background: white;
            color: black;
        }

        /* Light mode styles */
        body.light-mode {
            background-color: #f7f7f7;
            color: black;
        }

        body.light-mode #addon {
            background: rgba(255, 255, 255, 0.9);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        body.light-mode h2 {
            color: #555;
        }

        body.light-mode .provider-group {
            background: linear-gradient(90deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
        }

        body.light-mode button {
            background: #6c63ff;
            color: white;
        }

        body.light-mode .toggle-mode {
            border: 2px solid black;
            color: black;
        }

        body.light-mode .toggle-mode:hover {
            background: black;
            color: white;
        }
    </style>
</head>
<body>
    <button class="toggle-mode" onclick="toggleMode()">Switch to Light Mode</button>
    <div id="addon">
        <h1>Flow</h1>
        <h2>v1.5.0</h2>
        <p class="description">Configura i tuoi provider: Si noti che se si attiva la ricerca veloce i risultati saranno meno accurati ma più veloci.</p>
        <h3>Select Providers:</h3>
        <form id="provider-form">
            <div class="provider-group">
                <label for="streamingcommunity" class="provider-label">
                    <input type="checkbox" id="streamingcommunity"> StreamingCommunity
                </label>
            </div>
            <div class="provider-group">
                <label for="lordchannel" class="provider-label">
                    <input type="checkbox" id="lordchannel"> LordChannel
                </label>
            </div>
            <div class="provider-group">
                <label for="streamingwatch" class="provider-label">
                    <input type="checkbox" id="streamingwatch"> StreamingWatch
                </label>
            </div>
            <div class="provider-group">
                <label for="animeworld" class="provider-label">
                    <input type="checkbox" id="animeworld"> Animeworld
                </label>
            </div>
        </form>
        <button id="generateManifestButton">Generate Manifest</button>
    </div>
    <script>
        function toggleMode() {
            const body = document.body;
            const isLightMode = body.classList.toggle('light-mode');
            const toggleButton = document.querySelector('.toggle-mode');
            toggleButton.textContent = isLightMode ? 'Switch to Dark Mode' : 'Switch to Light Mode';
        }
    </script>
</body>
</html>
"""