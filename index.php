<!DOCTYPE html>
<html>
<head>
	<title>facebook_scrapy</title>
</head>
<body>
	<?php
		$city = isset($_REQUEST['city']) ? $_REQUEST['city'] : "";
		$category = isset($_REQUEST['category']) ? $_REQUEST['category'] : "";
		$page = isset($_GET['page']) ? $_GET['page'] : 1;
		/*echo $city;*/
		/*echo $category;*/
	?>
	<form action="index.php" method="post" id="target">
		City:<input type="text" id = "city" name="city" value="<?php echo $city; ?>">
		Category:<input type="text" id = "category" name="category" value="<?php echo $category; ?>">
		<input type="hidden" name="page" id="page" value="<?php echo $page;?>"/>
		<button id = "submit" name = "submit">Scrapy</button>
	</form>

	<?php
	$cmd = "python method.py";
	if($city != ""){
		$cmd = $cmd." ".$city;
		if($category != "")
			$cmd = $cmd." ".$category;
	}
	echo $cmd;
	$scrapy_data = json_decode(exec($cmd));
	?>
	<table>
		<thead>
			<th>id</th>
			<th>Product Name</th>
		</thead>
		<tbody>
			<?php foreach($scrapy_data as $key => $item):?>
				<?php if($key == $page+9) break;?>
				<tr>
					<td>
						<?php echo $key+1; ?>
					</td>
					<td>
						<?php echo $item; ?>
					</td>
				</tr>
			<?php endforeach;?>
		</tbody>
	</table>
	<a href="index.php?page=<?php echo ($page+10);?>&city=<?php echo $city;?>&category=<?php echo $category;?>">Load More</a>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script type="text/javascript">
	function form_submit(){
		var page = $('#page').val();
		//alert(page);
		page = parseInt(page)+10;
		alert(page);
		$('#page').val(page);
		$('#target').submit();
	}
</script>
</html>
