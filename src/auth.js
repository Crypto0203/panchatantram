// Cryptographic Vault Security Module
// The raw PIN is never stored, displayed, or transferred.
// Only the salted SHA-256 cryptographic digest is verified via the Web Crypto API.

const VAULT_SALT = 'panchatantra_kids_vault_salt_992187';
const VAULT_DIGEST = '9bead0629ec4acf294294893e09c2d740ae261ec8a3271f02069d6c4f480ecc1';
const SESSION_KEY = 'panchatantra_vault_session_token';

/**
 * Computes SHA-256 hash of a string using browser's native Web Crypto API
 */
async function computeSha256(text) {
  const msgUint8 = new TextEncoder().encode(text);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

/**
 * Verifies entered PIN against the salted cryptographic digest
 * @param {string} candidatePin 
 * @returns {Promise<boolean>}
 */
export async function verifyVaultPin(candidatePin) {
  if (!candidatePin || candidatePin.length !== 4) return false;
  try {
    const candidateHash = await computeSha256(VAULT_SALT + candidatePin);
    if (candidateHash === VAULT_DIGEST) {
      // Create session token with timestamp
      const sessionData = {
        authenticated: true,
        timestamp: Date.now(),
        token: await computeSha256(VAULT_DIGEST + Date.now().toString())
      };
      sessionStorage.setItem(SESSION_KEY, JSON.stringify(sessionData));
      return true;
    }
  } catch (err) {
    console.error('Cryptographic verification error:', err);
  }
  return false;
}

/**
 * Checks if user has an active authenticated session
 * @returns {boolean}
 */
export function isVaultUnlocked() {
  try {
    const stored = sessionStorage.getItem(SESSION_KEY);
    if (!stored) return false;
    const session = JSON.parse(stored);
    // Session valid for 12 hours
    const isValid = session && session.authenticated && (Date.now() - session.timestamp < 12 * 60 * 60 * 1000);
    if (!isValid) {
      sessionStorage.removeItem(SESSION_KEY);
      return false;
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Locks the vault and clears session
 */
export function lockVault() {
  sessionStorage.removeItem(SESSION_KEY);
}
