---
layout: default
title: Categories
type: tangibles
categories: [C1.4]
---

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fancy Folder Structure</title>
<style>
  /* Your CSS styles here */
  .folder {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .has-subfolder .subfolder {
    display: none;
  }
  .has-subfolder.active .subfolder {
    display: block;
  }
  .folder-header {
    cursor: pointer;
    display: flex;
    align-items: center;
  }
  .arrow {
    margin-right: 10px;
    transition: transform 0.3s;
  }
  .open {
    transform: rotate(90deg);
  }
</style>
</head>
<body>
<ul class="folder">
  <li class="has-subfolder">
    <div class="folder-header">
      <span class="arrow">▶</span>
      Lab Notebooks!
    </div>
    <ul class="subfolder">
      <li><a href="{{site.baseurl}}/c4.0/2023/08/21/Lab-Notebook-0.html">Lab Notebook 0</a></li>
      <li><a href="{{site.baseurl}}/c4.0/2023/08/23/Lab-Notebook-1.html">Lab Notebook 1</a></li>
      <li><a href="{{site.baseurl}}/c4.0/2023/08/27/Lab-Notebook-2.html">Lab Notebook 2</a></li>
    </ul>
  </li>
  <li class="has-subfolder">
    <div class="folder-header">
      <span class="arrow">▶</span>
      Folder 2
    </div>
    <ul class="subfolder">
      <li><a href="">Subfolder 2.1</a></li>
      <li><a href="">Subfolder 2.2</a></li>
    </ul>
  </li>
  <!-- More folder items here -->
</ul>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const folderHeaders = document.querySelectorAll('.folder-header');
    folderHeaders.forEach(header => {
      header.addEventListener('click', function() {
        const parentFolder = this.closest('.has-subfolder');
        parentFolder.classList.toggle('active');
        const arrow = this.querySelector('.arrow');
        arrow.classList.toggle('open');
      });
    });
  });
</script>
</body>