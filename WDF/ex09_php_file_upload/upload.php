<?php
if (isset($_POST['upload'])) {
    $uploadDir = "uploads/";
    $fileName  = $_FILES["image"]["name"];
    $fileTmp   = $_FILES["image"]["tmp_name"];
    $fileType  = $_FILES["image"]["type"];
    $fileError = $_FILES["image"]["error"];

    // Allowed image types
    $allowedTypes = array("image/jpeg", "image/png");

    if ($fileError === 0) {
        if (in_array($fileType, $allowedTypes)) {
            // Create uploads directory if it does not exist
            if (!is_dir($uploadDir)) {
                mkdir($uploadDir, 0777, true);
            }
            $targetFile = $uploadDir . basename($fileName);
            if (move_uploaded_file($fileTmp, $targetFile)) {
                echo "Image uploaded successfully!";
            } else {
                echo "Error uploading file.";
            }
        } else {
            echo "Only JPEG and PNG images are allowed.";
        }
    } else {
        echo "File upload error.";
    }
}
?>
