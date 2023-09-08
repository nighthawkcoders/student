---
toc: true
comments: true
layout: post
title: Markdown table
description: Table with Jquery that is pulling from a Covid-19 API!
type: tangibles
courses: { csa: {week: 2} }
categories: [C1.4]
---

<head>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>
<body>
    <table id="covidTable" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Country</th>
                <th>Continent</th>
                <th>New Cases</th>
                <th>Total Cases</th>
                <!-- Add more table headers for other data as needed -->
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    <script>
        const settings = {
            async: true,
            crossDomain: true,
            url: 'https://covid-193.p.rapidapi.com/statistics',
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': '1748ee8916mshe4a05c6edb7af0ap1399f4jsn23f82b0ddfa3',
                'X-RapidAPI-Host': 'covid-193.p.rapidapi.com'
            }
        };
        $.ajax(settings).done(function (response) {
            console.log(response);
            if (response && response.response) {
                const data = response.response;
                const table = $('#covidTable').DataTable({
                    data: data,
                    columns: [
                        { data: 'country' },
                        { data: 'continent' },
                        { data: 'cases.new' },
                        { data: 'cases.total' },
                        // Add more columns for other data as needed
                    ]
                });
            }
        });
    </script>
</body>
