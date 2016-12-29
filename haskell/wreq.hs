-- cabal update
-- cabal install -j --disable-tests wreq

{-# LANGUAGE OverloadedStrings #-}

import Control.Lens
import Data.Aeson.Lens (_Integer, _String, key)
import Data.Text.Encoding (encodeUtf8)

import Network.Wreq
import qualified Network.Wreq.Session as S

apiUrl = "https://api.masterleague.net"

apiUser = "username" :: String
apiPass = "password" :: String

main = S.withSession $ \s -> do

    -- Fetch authorization token for premium users
    let baseOpts = defaults & header "Accept" .~ ["application/json"]

    r1 <- S.postWith baseOpts s (apiUrl ++ "/auth/token/") ["username" := apiUser, "password" := apiPass]

    let token = r1 ^. responseBody . key "token" . _String

    -- Perform authenticated API requests
    let opts = baseOpts & auth ?~ oauth2Token (encodeUtf8 token)

    r2 <- S.getWith opts s (apiUrl ++ "/heroes/")

    let count = r2 ^? responseBody . key "count" . _Integer

    putStrLn $ "Found " ++ maybe "N/A" show count ++ " heroes!"
