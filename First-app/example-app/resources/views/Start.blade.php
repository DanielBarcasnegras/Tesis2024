<!DOCTYPE HTML>
<!--
	Hyperspace by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Hyperspace by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="{{ asset('assets/css/main.css') }}" />
		<noscript><link rel="stylesheet" href="{{ asset('assets/css/noscript.css') }}" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Sidebar -->
			<section id="sidebar">
				<div class="inner">
					<nav>
						<ul>
							<li><a href="#intro">Welcome</a></li>
							<li><a href="#one">Data insights</a></li>
							<li><a href="#two">Raw data</a></li>
						</ul>
					</nav>
				</div>
			</section>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Intro -->
					<section id="intro" class="wrapper style1 fullscreen fade-up">
						<div class="inner">
							<h1>Hyperspace</h1>
							<p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
							and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
							<ul class="actions">
								<li><a href="#one" class="button scrolly">Learn more</a></li>
							</ul>
						</div>
					</section>

				<!-- One -->
					<section id="one" class="wrapper style2 spotlights">
						<section>
							<a href="#" class="image"><img src="images/pic01.jpg" alt="" data-position="center center" /></a>
							<div class="content">
								<div class="inner">
									<h2>Sed ipsum dolor</h2>
									<p>Phasellus convallis elit id ullamcorper pulvinar. Duis aliquam turpis mauris, eu ultricies erat malesuada quis. Aliquam dapibus.</p>
									<ul class="actions">
										<li><a href="generic.html" class="button">Learn more</a></li>
									</ul>
								</div>
							</div>
						</section>
						<section>
							<a href="#" class="image"><img src="images/pic02.jpg" alt="" data-position="top center" /></a>
							<div class="content">
								<div class="inner">
									<h2>Feugiat consequat</h2>
									<p>Phasellus convallis elit id ullamcorper pulvinar. Duis aliquam turpis mauris, eu ultricies erat malesuada quis. Aliquam dapibus.</p>
									<ul class="actions">
										<li><a href="generic.html" class="button">Learn more</a></li>
									</ul>
								</div>
							</div>
						</section>
						<section>
							<a href="#" class="image"><img src="images/pic03.jpg" alt="" data-position="25% 25%" /></a>
							<div class="content">
								<div class="inner">
									<h2>Ultricies aliquam</h2>
									<p>Phasellus convallis elit id ullamcorper pulvinar. Duis aliquam turpis mauris, eu ultricies erat malesuada quis. Aliquam dapibus.</p>
									<ul class="actions">
										<li><a href="generic.html" class="button">Learn more</a></li>
									</ul>
								</div>
							</div>
						</section>
					</section>

				<!-- Two -->
					<section id="two" class="wrapper style3 fade-up">
						<div class="inner">
							<h2>Raw Data</h2>
							<p>Phasellus convallis elit id ullamcorper pulvinar. Duis aliquam turpis mauris, eu ultricies erat malesuada quis. Aliquam dapibus, lacus eget hendrerit bibendum, urna est aliquam sem, sit amet imperdiet est velit quis lorem.</p>
							<div class="features">
								<table>
									<thead>
										<tr>
											<th>Image Name</th>
											<th>ROI_A1_count</th>
											<th>ROI_A2_count</th>
											<th>ROI_A3_count</th>
											<th>ROI_A4_count</th>
											<th>ROI_A5_count</th>
											<th>ROI_A6_count</th>
											<th>ROI_A7_count</th>
											<th>ROI_A8_count</th>
											<th>ROI_B1_count</th>
											<th>ROI_B2_count</th>
											<th>ROI_B3_count</th>
											<th>ROI_B4_count</th>
											<th>ROI_B5_count</th>
											<th>ROI_B6_count</th>
											<th>ROI_B7_count</th>
											<th>ROI_B8_count</th>
											<th>Image Data</th>
										</tr>
									</thead>
									<tbody>
										@foreach ($images as $image)
											<tr>
												<td>{{ $image->image_name }}</td>
												<td>{{ $image->ROI_A1_count }}</td>
												<td>{{ $image->ROI_A2_count }}</td>
												<td>{{ $image->ROI_A3_count }}</td>
												<td>{{ $image->ROI_A4_count }}</td>
												<td>{{ $image->ROI_A5_count }}</td>
												<td>{{ $image->ROI_A6_count }}</td>
												<td>{{ $image->ROI_A7_count }}</td>
												<td>{{ $image->ROI_A8_count }}</td>
												<td>{{ $image->ROI_B1_count }}</td>
												<td>{{ $image->ROI_B2_count }}</td>
												<td>{{ $image->ROI_B3_count }}</td>
												<td>{{ $image->ROI_B4_count }}</td>
												<td>{{ $image->ROI_B5_count }}</td>
												<td>{{ $image->ROI_B6_count }}</td>
												<td>{{ $image->ROI_B7_count }}</td>
												<td>{{ $image->ROI_B8_count }}</td>
												<td>{{ $image->image_data }}</td>
											</tr>
										@endforeach
									</tbody>
								</table>
							</div>
						</div>
					</section>

		<!-- Footer -->
			<footer id="footer" class="wrapper style1-alt">
				<div class="inner">
					<ul class="menu">
						<li>&copy; Untitled. All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
					</ul>
				</div>
			</footer>

		<!-- Scripts -->
			<script src="{{ asset('assets/js/jquery.min.js') }}"></script>
			<script src="{{ asset('assets/js/jquery.scrollex.min.js') }}"></script>
			<script src="{{ asset('assets/js/jquery.scrolly.min.js') }}"></script>
			<script src="{{ asset('assets/js/browser.min.js') }}"></script>
			<script src="{{ asset('assets/js/breakpoints.min.js') }}"></script>
			<script src="{{ asset('assets/js/util.js') }}"></script>
			<script src="{{ asset('assets/js/main.js') }}"></script>

	</body>
</html>
