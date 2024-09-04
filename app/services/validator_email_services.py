from fastapi import HTTPException, status


def validation_format_email(email):
    
    from email_validator import validate_email, EmailUndeliverableError
    
    try:
        validate_email(email)
        return True
    except EmailUndeliverableError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"E-amil is incorrect: {e}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"E-amil is incorrect: {e}")