# static.py

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flow</title>
    <link rel="icon" href="https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f4fd.svg" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
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
            color: #333;
            background-color: #f3f3f3;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        body.dark-mode {
            background-color: #121212;
            color: #ffffff;
        }

        #addon {
            background: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 90%;
            text-align: center;
        }

        body.dark-mode #addon {
            background: #1e1e1e;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        h1 {
            font-size: 1.8rem;
            margin-bottom: 10px;
        }

        h2 {
            font-size: 0.9rem;
            font-weight: 300;
            margin-bottom: 20px;
        }

        .provider-group {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #ff7eb3, #ff758c);
            border-radius: 8px;
            padding: 10px;
            transition: transform 0.2s ease;
        }

        .provider-group:hover {
            transform: scale(1.02);
        }

        .provider-label {
            font-size: 0.95rem;
            font-weight: 400;
            color: #fff;
        }

        .provider-group input[type="checkbox"] {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }

        button {
            border: none;
            outline: none;
            background-color: #6200ea;
            color: #fff;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #3700b3;
        }

        button:active {
            background-color: #bb86fc;
        }

        #manifestBox {
            margin-top: 15px;
            padding: 10px;
            background-color: #ececec;
            border-radius: 5px;
            text-align: left;
            font-size: 0.9rem;
            display: none;
            color: #000;
        }

        body.dark-mode #manifestBox {
            background-color: #2e2e2e;
            color: #fff;
        }

        #switchMode {
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 8px 12px;
            font-size: 0.85rem;
            border-radius: 5px;
            background-color: #ddd;
            cursor: pointer;
        }

        body.dark-mode #switchMode {
            background-color: #444;
            color: #fff;
        }
    </style>
</head>
<body>
    <div id="switchMode">Switch to Dark Mode</div>
    <div id="addon">
        <h1>Flow</h1>
        <h2>v1.5.0</h2>
        <p>Configura i tuoi provider: Si noti che se si attiva la ricerca veloce i risultati saranno meno accurati ma più veloci.</p>
        <h3>Select Providers:</h3>
        <form id="provider-form">
            <div class="provider-group">
                <label for="streamingcommunity" class="provider-label">
                    StreamingCommunity
                </label>
                <input type="checkbox" id="streamingcommunity">
            </div>
            <div class="provider-group">
                <label for="lordchannel" class="provider-label">
                    LordChannel
                </label>
                <input type="checkbox" id="lordchannel">
            </div>
            <div class="provider-group">
                <label for="streamingwatch" class="provider-label">
                    StreamingWatch
                </label>
                <input type="checkbox" id="streamingwatch">
            </div>
            <div class="provider-group">
                <label for="animeworld" class="provider-label">
                    Animeworld
                </label>
                <input type="checkbox" id="animeworld">
            </div>
        </form>
        <button id="generateManifestButton">Generate Manifest</button>
        <div id="manifestBox"></div>
    </div>
    <script>
        // Dark Mode Toggle
        const switchMode = document.getElementById("switchMode");
        const body = document.body;

        switchMode.addEventListener("click", () => {
            body.classList.toggle("dark-mode");
            switchMode.textContent = body.classList.contains("dark-mode") ? "Switch to Light Mode" : "Switch to Dark Mode";
        });

        // Generate Manifest Functionality
        const generateManifestButton = document.getElementById("generateManifestButton");
        const manifestBox = document.getElementById("manifestBox");

        generateManifestButton.addEventListener("click", () => {
            const selectedProviders = [];
            document.querySelectorAll("#provider-form input[type='checkbox']").forEach((checkbox) => {
                if (checkbox.checked) {
                    selectedProviders.push(checkbox.id);
                }
            });

            if (selectedProviders.length === 0) {
                manifestBox.textContent = "No providers selected.";
                manifestBox.style.display = "block";
                return;
            }

            const manifestUrl = `https://flow-3qre.onrender.com/${selectedProviders.join("|")}`;
            manifestBox.textContent = `Generated Manifest URL: \n${manifestUrl}`;
            manifestBox.style.display = "block";
        });
    </script>
</body>
</html>
"""