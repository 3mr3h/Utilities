$path_ = Read-Host "Please enter the file path for hash calculation"

Function Get-HashType {
    $type=Read-Host "
        1 - MD5
        2 - SHA1
        3 - SHA256
        4 - SHA512
        Please choose "
    Switch ($type) {
        1 {$choice="MD5"}
        2 {$choice="SHA1"}
        3 {$choice="SHA256"}
        4 {$choice="SHA512"}    
    }
    return $choice
}

$sha_ = Get-HashType

get-fileHash -Algorithm $sha_ $path_| Format-List