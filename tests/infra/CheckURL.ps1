function Check-Response
{
    try
    {
        # First we create the request.
        $HTTP_Request = [System.Net.WebRequest]::Create('http://localhost:8080')
        # We then get a response from the site.
        $HTTP_Response = $HTTP_Request.GetResponse()
        # We then get the HTTP code as an integer.
        $HTTP_Status = [int]$HTTP_Response.StatusCode
        # Finally, we clean up the http request by closing it.
        If ($HTTP_Response -ne $null)
        {
            $HTTP_Response.Close()
        }
        return $HTTP_Status
    }
    catch
    {
        return 0
    }

}

$HTTP_Status = Check-Response
$Retries = 1
while ($HTTP_Status -ne 200)
{
    Write-Host "---------------> BRINGING UP (Number of retries: $retries)"
    sleep 5
    $HTTP_Status = Check-Response
    $Retries++
}
Write-Host "===================================================="
Write-Host "=================== Site is OK! ===================="
Write-Host "===================================================="
