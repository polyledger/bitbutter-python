echo "\033[32mDeleting Bitbutter user $1...\033[0m\n"

timestamp=$(date +%s000)
method=DELETE
route=/v1/users/$1
signature=$(python get_signature.py $timestamp $method $route)

curl --request $method \
  --url "${BITBUTTER_BASE_URI}${route}" \
  --header "BB-ACCESS-KEY: ${BITBUTTER_API_KEY}" \
  --header "BB-ACCESS-SIGN: ${signature}" \
  --header "BB-PARTNER-ID: ${BITBUTTER_PARTNER_ID}" \
  --header "BB-TIMESTAMP: ${timestamp}" | json_pp
