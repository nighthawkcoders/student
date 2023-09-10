---
comments: false
layout: post
title: Search Britanica
description: View any image
type: hacks
courses: {'compsci': {'week': 3}}
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Britannica Search</title>
</head>
<body>
    <h1>Britannica Search</h1>
    
    <!-- Input field for search query -->
    <input type="text" id="searchQuery" placeholder="Enter your search query">
    <button onclick="searchBritannica()">Search</button>

    <!-- Display search results here -->
    <div id="searchResults"></div>

    <!-- Link to the external JavaScript file -->
    <script src="britannica_search.js"></script>
</body>
</html>
