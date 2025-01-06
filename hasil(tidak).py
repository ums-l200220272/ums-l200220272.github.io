from metaflow import Flow

# Mengambil data dari run terakhir
run = Flow('ManyKmeansFlow').latest_run
k3 = run.data.results[3]  # 3 Clusters
k4 = run.data.results[4]  # 4 Clusters
k5 = run.data.results[5]  # 5 Clusters

# Fungsi untuk menulis hasil ke dalam HTML
def generate_html(k3, k4, k5):
    html_content = """
    <html>
    <head>
        <title>Clustering Results</title>
        <style>
            body { font-family: 'Arial', sans-serif; margin: 20px; background-color: #f4f4f4; }
            h1 { color: #2E8B57; text-align: center; padding: 20px; }
            h2 { color: #333; text-align: center; margin-top: 40px; }
            .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            .cluster-card {
                background-color: #ffffff;
                padding: 20px;
                width: 250px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s;
            }
            .cluster-card:hover {
                transform: scale(1.05);
            }
            .cluster-card h3 {
                color: #4CAF50;
                font-size: 18px;
                margin-bottom: 15px;
            }
            .cluster-card ul {
                list-style-type: none;
                padding-left: 0;
            }
            .cluster-card li {
                color: #333;
                font-size: 16px;
                padding: 5px 0;
            }
            .cluster-card ul li::before {
                content: "🔹";
                margin-right: 10px;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
                color: #777;
            }
        </style>
    </head>
    <body>

        <h1>Clustering Results</h1>

        <h2>Results for 3, 4, and 5 Clusters</h2>

        <div class="container">

            <!-- 3 Clusters Section -->
            <div class="cluster-card">
                <h3>3 Clusters</h3>
                <ul>"""
    
    # Menambah hasil clustering 3 clusters
    for i, top_terms in enumerate(k3):
        html_content += f"<li><strong>Cluster {i + 1}:</strong> {', '.join(top_terms)}</li>"

    html_content += """
                </ul>
            </div>

            <!-- 4 Clusters Section -->
            <div class="cluster-card">
                <h3>4 Clusters</h3>
                <ul>"""
    for i, top_terms in enumerate(k4):
        html_content += f"<li><strong>Cluster {i + 1}:</strong> {', '.join(top_terms)}</li>"

    html_content += """
                </ul>
            </div>

            <!-- 5 Clusters Section -->
            <div class="cluster-card">
                <h3>5 Clusters</h3>
                <ul>"""
    for i, top_terms in enumerate(k5):
        html_content += f"<li><strong>Cluster {i + 1}:</strong> {', '.join(top_terms)}</li>"

    html_content += """
                </ul>
            </div>
        </div>

        <div class="footer">
            <p>Clustering completed using KMeans for 3, 4, and 5 clusters. This analysis was generated using Metaflow.</p>
        </div>

    </body>
    </html>
    """

    return html_content

# Menulis hasil ke dalam file HTML
html_result = generate_html(k3, k4, k5)

with open('clustering_results.html', 'w') as file:
    file.write(html_result)

print("HTML file generated: clustering_results.html")
