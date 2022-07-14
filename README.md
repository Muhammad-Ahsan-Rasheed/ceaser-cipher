</head>
<body><p>&nbsp;</p>
<h1 id='python-code-for-ceaser-cipher'>Python Code for Ceaser Cipher</h1>

- [Python Code for Ceaser Cipher](#python-code-for-ceaser-cipher)
  * [Caesar cipher](#caesar-cipher)
  * [Example](#example)
- [How this code is working?](#how-this-code-is-working)
  * [List Comprehension](#list-comprehension)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


<p><img alt="GitHub followers" src="https://img.shields.io/github/followers/Muhammad-Ahsan-Rasheed?style=social"> 	</p>
<h2 id='caesar-cipher'>Caesar cipher</h2>
<p>In <a href='https://en.wikipedia.org/wiki/Cryptography'>cryptography</a>, a <strong>Caesar cipher</strong>, also known as <strong>Caesar&#39;s cipher</strong>, the <strong>shift cipher</strong>, <strong>Caesar&#39;s code</strong> or <strong>Caesar shift</strong>, is one of the simplest and most widely known <a href='https://en.wikipedia.org/wiki/Encryption'>encryption</a> techniques.</p>
<h2 id='example'>Example</h2>
<p>The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the <a href='https://en.wikipedia.org/wiki/Key_(cryptography)'>key</a>):</p>
<figure><table>
<thead>
<tr><th style='text-align:center;' >Plain</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th><th>L</th><th>M</th><th>N</th><th>O</th><th>P</th><th>Q</th><th>R</th><th>S</th><th>T</th><th>U</th><th>V</th><th>W</th><th>X</th><th>Y</th><th>Z</th></tr></thead>
<tbody><tr><td style='text-align:center;' >Cipher</td><td>X</td><td>Y</td><td>Z</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td></tr></tbody>
</table></figure>
<p>When encrypting, a person looks up each letter of the message in the &quot;plain&quot; line and writes down the corresponding letter in the &quot;cipher&quot; line.</p>
<pre><code>Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
</code></pre>
<h1 id='how-this-code-is-working'>How this code is working?</h1>
<p>The code has three main functions:</p>
<ol>
<li>encrypt - to encrypt the text</li>
<li>decrypt - to decrypt the text</li>
<li>filing - to read, write the file and perform encryption and decryption</li>

</ol>
<p>&nbsp;</p>
<p><code>P.S: It will only encrypt the alphabets, not numbers.</code></p>
<p><strong>I used list comprehension for one line code. If you want to know more about check this out</strong> </p>
<h2 id='list-comprehension'>List Comprehension</h2>
<p><a href='https://blog.devgenius.io/is-list-comprehension-the-most-effective-way-to-solve-any-tasks-python-b6bb3f5391fa'>List Comprehension Effective Way to Solve Tasks?</a></p>
<p>Follow for more updates...</p>
<p>Want to collaborate? Let’s catch up! 💀</p>
<p>Happy Coding 😄</p>
</body>
</html>
