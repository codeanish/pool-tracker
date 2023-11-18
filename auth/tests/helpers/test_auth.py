from datetime import datetime, timedelta

import pytest
from auth.helpers.auth import create_access_token, verify_password
from auth.schemas.token import TokenClaims
from passlib.exc import UnknownHashError

def test_create_access_token():
    # Test case 1: Valid token claims
    claims = TokenClaims(sub="user_id", exp=datetime.utcnow() + timedelta(minutes=30))
    token = create_access_token(claims)
    assert isinstance(token, str)
    assert len(token) > 0

    # Test case 2: Token expiration time in the past
    claims = TokenClaims(sub="user_id", exp=datetime.utcnow() - timedelta(minutes=30))
    token = create_access_token(claims)
    assert isinstance(token, str)
    assert len(token) > 0

    # Test case 3: Token expiration time in the future
    claims = TokenClaims(sub="user_id", exp=datetime.utcnow() + timedelta(days=7))
    token = create_access_token(claims)
    assert isinstance(token, str)
    assert len(token) > 0


def test_correct_password():
    # Test case for correct password
    password = "password123"
    hashed_password = '$2b$12$DgDEqCLYBynMtE94Xo.z5uBMYpO./IWKPEConEcu/.plUmbqKTkiq'
    result = verify_password(password, hashed_password)
    assert result == True

def test_incorrect_password():
    # Test case for incorrect password
    password = "wrongpassword"
    hashed_password = '$2b$12$DgDEqCLYBynMtE94Xo.z5uBMYpO./IWKPEConEcu/.plUmbqKTkiq'
    result = verify_password(password, hashed_password)
    assert result == False

def test_empty_password():
    # Test case for empty password
    password = ""
    hashed_password = '$2b$12$DgDEqCLYBynMtE94Xo.z5uBMYpO./IWKPEConEcu/.plUmbqKTkiq'
    result = verify_password(password, hashed_password)
    assert result == False

def test_empty_hashed_password():
    # Test case for empty hashed password
    password = "password123"
    hashed_password = ""
    with pytest.raises(UnknownHashError):
        verify_password(password, hashed_password)
    # assert result == False

