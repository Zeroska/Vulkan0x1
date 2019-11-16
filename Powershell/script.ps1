

if ($args.count -ne 1) {
  Write-Host "Missing Parameter!" -foregroundcolor "Red"
  exit
}


$folderpath = $args[0]

Write-Host ("Directory listing of "+ $folderpath)


#Process each item in the directory 

foreach ($i in get-childitem $folderpath){
  if ($i.mode.substring(0,1) -eq "d") {
    Write-Host $i.name -foregroundcolor "Yellow"
  } else {
    Write-Host $i.name - foregroundcolor "Green"
  }
}
