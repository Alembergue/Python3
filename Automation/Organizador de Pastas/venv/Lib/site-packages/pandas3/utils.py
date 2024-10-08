def select(session, bucket, file, sql, header):
    req = session.select_object_content(
        Bucket=bucket,
        Key=file,
        ExpressionType='SQL',
        Expression=sql,
        InputSerialization={'CSV': {'RecordDelimiter': '\r\n', 'FileHeaderInfo': header}},
        OutputSerialization={'CSV': {}},
    )

    records = []

    for event in req['Payload']:
        if 'Records' in event:
            records.append(event['Records']['Payload'])

    file_str = ''.join(r.decode('utf-8') for r in records)

    return file_str
